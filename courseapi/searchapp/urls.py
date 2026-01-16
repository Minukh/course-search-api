
from django.urls import path

from .views import CourseCreate, CourseList, CourseSearchView

urlpatterns = [
    path("course_create/",CourseCreate.as_view()),
    path("course_list/",CourseList.as_view()),
    path("search/",CourseSearchView.as_view()),
]