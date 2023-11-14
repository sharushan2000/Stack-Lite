from django.contrib import admin
from .models import Content ,ContentType

# Register your models here.
admin.site.register(ContentType)
admin.site.register(Content)
