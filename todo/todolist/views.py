
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from rest_framework import viewsets, permissions
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.authentication import JWTAuthentication
from todolist.authentication import RemoteJWTAuthentication
from rest_framework.permissions import IsAuthenticated
from todolist.models import Tasks
from todolist.serializers import TaskSerializer
from django.conf import settings

ACCOUNT_SERVICE_TOKEN_URL = "http://accounts:8000/token/"  # account service host

# --------------------
# REST API endpoints
# --------------------
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    authentication_classes = [RemoteJWTAuthentication]
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Tasks.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)

def login_view(request):
    print('I am in login')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Ask account_service for JWT
        resp = requests.post(ACCOUNT_SERVICE_TOKEN_URL, json={"username": username, "password": password})
        if resp.status_code != 200:
            return render(request, "login.html", {"error": "Invalid credentials"})

        token = resp.json()["access"]

        # Decode JWT
        backend = TokenBackend(algorithm="HS256", signing_key=settings.SIMPLE_JWT['SIGNING_KEY'])
        payload = backend.decode(token, verify=True)
        user_id = payload["user_id"]

        # Save to session
        request.session["jwt"] = token
        request.session["user_id"] = user_id
        request.session["username"] = username

        return redirect("todolist:home")

    return render(request, "login.html",)

def home(request):
    # Check if user is logged in via JWT stored in session
    token = request.session.get("jwt")
    if not token:
        print('Redirect to login')
        return redirect("todolist:login")  # If no token, redirect to login page

    
    username = request.session.get("username")
    user_id = request.session.get("user_id")
    
    return render(request, "home.html", {"username": username,"token":token,"user_id":user_id})

def logout_view(request):
    request.session.flush()  
    return redirect("todolist:login")

ACC_API_REGISTER_URL = "http://accounts:8000/register/"  
def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Call the API endpoint
        resp = requests.post(ACC_API_REGISTER_URL, json={
            "username": username,
            "password": password
        })

        if resp.status_code == 201:
            return render(request, "register.html", {"success": "To-do list user created successfully!"})
        else:
            return render(request, "register.html", {"error": resp.json(),})

    return render(request, "register.html")