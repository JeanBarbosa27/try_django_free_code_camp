from django.urls import path

from .views import (
    CourseFormView,
    CoursesListView,
    CoursesView,
)

app_name = 'courses'

urlpatterns = [
    path('generic/', CoursesView.as_view(template_name='course_generic.html'), name='generic'),

    path('', CoursesListView.as_view(), name='index'),
    path(
        '<int:course_id>',
        CoursesView.as_view(template_name='course_detail.html'),
        name='course_detail'
    ),
    path(
        'add/',
        CourseFormView.as_view(page_title='Create a new course'),
        name='course_create'
    ),
    path(
        '<int:course_id>/update/',
        CourseFormView.as_view(page_title='Update course'),
        name='course_update'
    ),
]
