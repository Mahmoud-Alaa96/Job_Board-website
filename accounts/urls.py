from django.urls import path , include
from . import views
app_name = "accounts"
urlpatterns = [
 
    path("singup", views.singup , name= "singup"),
    path("profile", views.profile , name= "profile"),
    path("profile/edit", views.profile_edit , name= "profile_edit"),
]
 