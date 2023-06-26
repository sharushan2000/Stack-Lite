from django.contrib import admin
from django.urls import path
from user_handling import views
from django.conf import settings
from django.conf.urls.static import static


app_name ="user_handling"

urlpatterns = [
   path ("login/",views.user_login , name ="user_login"),
   path ("register/",views.user_register , name ="register"),
   path ("logout/",views.user_logout , name ="user_logout"),
   path("profile/",views.user_detail ,name="user_detail"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
