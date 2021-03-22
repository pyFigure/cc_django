{%- if cookiecutter.use_swagger.lower() == 'y' %}
from drf_yasg2.utils import swagger_auto_schema
{%- endif %}
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from demo.serializers import ApiSerializer, A, ASerializer, DemoSerializer, LongTimeTaskSerializer
from demo.tasks import long_time_task
from utils.drf.mixins import MultiSerializersMixin


class Demo1(APIView):
    """
    Demo1 用来展示 HTTP 各种操作
    支持: ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    """

    # 隐藏该类提供的所有接口
    # swagger_schema = None

    {%- if cookiecutter.use_swagger.lower() == 'y' %}
    @swagger_auto_schema(query_serializer=DemoSerializer)
    {%- endif %}
    def get(self, request, *args, **kwargs) -> Response:
        """
        ## 新增用户的接口
        ## 请求方法
            - post
        ## 请求格式
            - json
        ## 请求参数
        | 字段名| 含义  | 类型   | 是否必填   |  示例  |
        |:------:|:------:|:------:|:------:|:------:|
        | name | 姓名    |  string |是 | 李白 |
        ## 返回参数
        | 字段名| 含义  | 类型   |
        |:------:|:------:|:------:|
        | status | 状态码    |  str |
        | data | 数据  |  dict |
        ## 返回格式
            -json
        ## 返回示例
            - {"result": "ok", "data":{}}
        """
        return Response(data='get demo1', status=status.HTTP_200_OK)

    {%- if cookiecutter.use_swagger.lower() == 'y' %}
    @swagger_auto_schema(request_body=DemoSerializer)
    {%- endif %}
    def post(self, request, *args, **kwargs) -> Response:
        """post data from api"""
        return Response(data='post demo1', status=status.HTTP_200_OK)


class Demo2(APIView):
    """
    接口认证演示
    @authentication_classes: 认证类列表，任意类认证通过即可
    @permission_classes: 权限类列表，任意鉴权失败即不可
    """
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    {%- if cookiecutter.use_swagger.lower() == 'y' %}
    @swagger_auto_schema(query_serializer=ApiSerializer)
    {%- endif %}
    def post(self, request, *args, **kwargs) -> Response:
        """装饰器参数 auto_schema=None 隐藏单个接口"""
        return Response(data='get demo2', status=status.HTTP_200_OK)


class Demo3(GenericViewSet):
    """
    自定义序列化器及 JSON Schema 校验
    """
    serializer_class = DemoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data="create success", status=status.HTTP_200_OK)

    @action(methods=['POST'], detail=False)
    {%- if cookiecutter.use_swagger.lower() == 'y' %}
    @swagger_auto_schema(request_body=LongTimeTaskSerializer)
    {%- endif %}
    def exec_long_time_task(self, request, *args, **kwargs):
        """示例: 执行长时间任务"""
        serializer = LongTimeTaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = long_time_task.delay(**serializer.data)
        return Response(data={'task_id': task.id}, status=status.HTTP_200_OK)


class Demo4(MultiSerializersMixin, GenericViewSet):
    """
    为不同的方法指定不同的序列化器
    """
    serializer_class = {
        "default": DemoSerializer,
        "create": DemoSerializer
    }

    {%- if cookiecutter.use_swagger.lower() == 'y' %}
    @swagger_auto_schema(deprecated=True)
    {%- endif %}
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data="create success", status=status.HTTP_200_OK)


class Demo5(ModelViewSet):
    """
    基于模型的接口示范
    """
    queryset = A.objects.all()
    serializer_class = ASerializer

    # 隐藏全部 API 有效
    # swagger_schema = None

    {%- if cookiecutter.use_swagger.lower() == 'y' %}
    @swagger_auto_schema(auto_schema=None, deprecated=True)
    {%- endif %}
    def delete(self, request, *args, **kwargs) -> Response:
        """
        !!! 在 ModelViewSet 下，隐藏单个 API 无效
        !!! 在 ModelViewSet 下，deprecated 单个 API 无效
        """
        return Response(data='get demo2', status=status.HTTP_200_OK)
