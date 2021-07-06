# testserializer/models.py
from django.db import models
# 설명만을 위한 모델로, 상당히 대충 작성 되었습니다:)
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    email = models.CharField(max_length=100)