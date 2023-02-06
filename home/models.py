from django.conf import settings
from django.db import models
class Course(models.Model):
    'Generated Model'
    courseName = models.TextField()
    courseId = models.UUIDField(null=True,blank=True,)
