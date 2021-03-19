"""
ASerializer, BSerializer, ABSerializer: 展示多对多关系的的序列化
"""

from rest_framework import serializers

from demo.models import A, AB
from utils.drf.validators import JsonSchemaValidator


class ApiSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, help_text='your name in string')
    age = serializers.IntegerField(required=False, help_text='年龄', default=20)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


class ABSerializer(serializers.ModelSerializer):
    class Meta:
        model = AB
        fields = '__all__'


class ASerializer(serializers.ModelSerializer):
    m2m = ABSerializer(many=True, read_only=True, source='ab_set')

    class Meta:
        model = A
        fields = '__all__'


demo_info_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "high": {"type": "number", "minimum": 1, "maximum": 2.5},
        "weight": {"type": "number"},
        "aaa": {
            "type": "list",
        }
    },
    "required": ['high', 'weight']
}


class DemoSerializer(serializers.Serializer):
    """
    必须实现 update, create 方法, 在 serializer.save() 方法中会被调用
    """
    name = serializers.CharField(required=True, label="名称", help_text="这里是说明文档")
    age = serializers.IntegerField(label="年龄", help_text="芳龄几何?", max_value=100, min_value=1)
    info = serializers.JSONField(label="其他", help_text="JSON 数据", required=True,
                                 validators=[JsonSchemaValidator(schema=demo_info_schema)])

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class LongTimeTaskSerializer(serializers.Serializer):
    """长任务参数序列化器"""
    x = serializers.IntegerField(label='x')
    y = serializers.IntegerField(label='y')

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
