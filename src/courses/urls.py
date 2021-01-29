from django.urls import path

from .views import CoursesView

app_name = 'courses'

urlpatterns = [
    path('', CoursesView.as_view(), name='index'),
    path('<int:course_id>', CoursesView.as_view(template_name='course_detail.html'), name='course_detail')
]
