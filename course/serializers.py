from .models import Course
from rest_framework import serializers


class GetAllCourseSerialier(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title']
