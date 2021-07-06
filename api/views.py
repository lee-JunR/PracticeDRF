from django.shortcuts import render

# api/view.py

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

@api_view(['GET']) #해당 함수 view 에서 처리할 http 메소드
def HelloAPI(request):
    return Response("hello world!") #http response 형태로 return

