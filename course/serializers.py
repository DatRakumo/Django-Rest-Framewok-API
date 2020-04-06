from .models import Course
from rest_framework import serializers


class GetAllCourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title']

class CourseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    price = serializers.IntegerField(default=0)
    content = serializers.CharField(max_length=255)
