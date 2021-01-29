from django.db import models
from django.urls import reverse

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:course_detail', kwargs={"course_id": self.id})
