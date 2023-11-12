from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Content(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="content_profile")
    title = models.CharField(max_length=200)
    programing_language = models.CharField(max_length=20)
    course_name = models.CharField(max_length=50 ,blank=True)
    short_des = models.TextField(max_length=100)
    describe = models.TextField(max_length=750)
    code = models.TextField(max_length=500)
    screenshot = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    github = models.URLField(blank=True)


    class Meta:
        ordering = ("-created_date",)

    def __str__(self) -> str:
        return self.title +" " +self.user.username