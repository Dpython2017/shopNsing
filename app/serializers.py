from rest_framework import serializers


class UserCategorySerializer(serializers.Serializer):
    category = serializers.CharField(max_length=200)
