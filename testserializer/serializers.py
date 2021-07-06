# test/serializers.py
from rest_framework import serializers
from .models import Person

# ModelSerializer 뒤에서 설명합니다.
class BasePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'phone', 'addr')

# ModelSerializer 뒤에서 설명합니다.
class EmailPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'email')


# serializers 의 인수를 ModelSerializer 가 아니라 Serializer 로 받는다면
# class BasePersonSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     phone = serializers.CharField()
#     addr = serializers.CharField()
#
#     def create(self, validated_data):
#         """
#         검증한 데이터로 새 `Person` 인스턴스를 생성하여 리턴합니다.
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         검증한 데이터로 기존 `Person` 인스턴스를 업데이트한 후 리턴합니다.
#         """
#         ...
#         ...
#         return instance