from django.shortcuts import render
from django.views import View
from rest_framework.response import Response
from  rest_framework import generics, status
from rest_framework.views import APIView

from .models import Course
from .serializer import CourseCreateSerializer
from .utils import CourseSearchHelper


class CourseCreate(generics.CreateAPIView):
    serializer_class = CourseCreateSerializer

    def post(self, request):
        try:
            serializer= CourseCreateSerializer(data=request.data)
            if serializer.is_valid():
                course = serializer.save()
                CourseSearchHelper().update_cached_tokens(course)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(CourseCreateSerializer(course).data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CourseList(generics.ListAPIView):
    def get(self, request):
        courses= Course.objects.all()
        serializer_class = CourseCreateSerializer(courses, many=True)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

class CourseSearchView(APIView):
    serializer_class = CourseCreateSerializer
    def get(self,request):
        query= request.query_params.get('q',"")
        helper=CourseSearchHelper()
        courses = helper.search_courses(query)
        serializer =CourseCreateSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
