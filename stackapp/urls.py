from django.contrib import admin
from django.urls import path
from stackapp import views
from django.conf import settings
from django.conf.urls.static import static


app_name ="stackapp"

urlpatterns = [
    path('recent/',views.QuestionList.as_view(),name="list_questions"),
    path('ask/',views.create_ticket ,name="ask_questions"),
    path('query/',views.SearchQuestionList.as_view(),name="search_result"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
