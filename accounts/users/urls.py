from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView

app_name = "users"

urlpatterns = [
    
    path("register/", views.RegisterView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

   
]
urlpatterns = format_suffix_patterns(urlpatterns)