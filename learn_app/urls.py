from django.urls import path
from . import views



app_name ="learn_app"

urlpatterns = [
    path('',views.ContentList.as_view() ,name="list"),

]
