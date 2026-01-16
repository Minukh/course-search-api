from .models import Course
from rest_framework import serializers

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:

        model = Course
        fields = ['id', 'name', 'description','course_price']

class CourseMinimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ["id", "name", "description", "course_price"]