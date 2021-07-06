from django.shortcuts import render

# Create your views here.
# test/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person
from .serializers import BasePersonSerializer, EmailPersonSerializer

@api_view(['GET'])
def PersonAPI(request, id):
    now_person = Person.object.get(id=id)
    serializer = BasePersonSerializer(now_person)
    return Response(serializer.data)
# => id=1에 대해 리턴된 Response: {'id': 1, 'name': '태뽕', 'phone': '01012345678', 'addr': '주소주소'}

@api_view(['GET'])
def EmailAPI(request, id):
    now_person = Person.object.get(id=id)
    serializer = EmailPersonSerializer(now_person)
    return Response(serializer.data)
# => id=1에 대해 리턴된 Response: {'id': 1, 'email': 'email@email.com'}