from account.models import User
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    """用户列表序列化器"""

    class Meta:
        model = User
        fields = ['id', 'name', 'cn_name', 'name', 'avatar', 'wx', 'mobile']
