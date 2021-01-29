from django.views import View
from django.shortcuts import render, get_object_or_404

from .models import Course


class CoursesView(View):
    template_name = 'courses_list.html'

    def get(self, request, course_id=None, *args, **kwargs):
        context = {
            'page_title': 'Courses',
        }

        if course_id:
            course = get_object_or_404(Course, id=course_id)
            context['course'] = course
            context['page_title'] = f"Course {course}"
        else:
            courses = Course.objects.all()
            context['courses'] = courses

        return render(request, self.template_name, context)
