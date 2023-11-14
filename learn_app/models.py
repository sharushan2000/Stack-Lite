from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ContentType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    



class Content(models.Model):
    title = models.CharField(max_length=200)
    content_type = models.ForeignKey(ContentType , on_delete=models.CASCADE , related_name="content_type")
    describe = models.TextField(max_length=500)
    code = models.TextField(max_length=1500)
    created_date = models.DateTimeField(auto_now=True)
    github = models.URLField(blank=True)

    class Meta:
        ordering = ("-created_date",)

    def __str__(self) -> str:
        return self.title




