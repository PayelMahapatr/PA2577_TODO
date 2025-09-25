from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = "todolist"

urlpatterns = [
    
    path("", views.login_view, name="login"),
     path("logout/", views.logout_view, name="logout"),
     path("home/", views.home, name="home"),
      path("register_page/", views.register_page, name="register_page"),

   
]
urlpatterns = format_suffix_patterns(urlpatterns)