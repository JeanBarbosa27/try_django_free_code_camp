from django.views import View
from django.shortcuts import render, get_object_or_404, redirect

from .models import Course
from .forms import CourseForm


class CoursesView(View):
    template_name = 'course_generic.html'

    def get(self, request, course_id=None, *args, **kwargs):
        context = {}

        if course_id:
            course = get_object_or_404(Course, id=course_id)
            context['course'] = course
            context['page_title'] = f"Course {course}"

        return render(request, self.template_name, context)


class CoursesListView(View):
    template_name = 'courses_list.html'
    courses = Course.objects.all()

    def get(self, request, *args, **kwargs):
        context = {
            'courses': self.courses,
            'page_title': 'Courses'
        }

        return render(request, self.template_name, context)

class CourseFormView(View):
    page_title = ''
    template_name = 'course_form.html'

    def get_form(self, request):
        course_id = self.kwargs.get('course_id')

        if course_id:
            course_object = get_object_or_404(Course, id=course_id)
            form = {
                'GET': CourseForm(instance=course_object),
                'POST': CourseForm(request.POST, instance=course_object)
            }

            return form[request.method]

        else:
            form = {
                'GET': CourseForm(),
                'POST': CourseForm(request.POST)
            }

            return form[request.method]

    def get(self, request, *args, **kwargs):
        form = self.get_form(request)

        context = {
            'form': form,
            'page_title': self.page_title,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.get_form(request)
        if form.is_valid():
            form.save()
            return redirect('courses:index')

        context = {
            'form': form,
            'page_title': self.page_title,
        }

        return render(request, self.template_name, context)
