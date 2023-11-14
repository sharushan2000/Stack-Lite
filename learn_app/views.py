from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import ContentType,Content


# Create your views here.
def list(request):
    return render (request , "learn_app/check.html")

class ContentList(ListView):
    model= Content
    paginate_by = 20
    template_name = "learn_app/list_content.html"
    context_object_name = "content_list"



def contentpage(request ,id):
    obj = Content.objects.get(pk=id)
    

