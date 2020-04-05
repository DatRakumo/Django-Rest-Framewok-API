# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import GetAllCourseSerialier


# Create your views here.

class GetAllCourseAPIView(APIView):

    def get(self,request):
        list_course = Course.objects.all()
        mydata = GetAllCourseSerialier(list_course, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

