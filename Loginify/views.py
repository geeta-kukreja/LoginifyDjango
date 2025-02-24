from django.shortcuts import render , redirect

from django.http import HttpResponse, JsonResponse
from .models import UserDetails
from django.contrib.auth.hashers import check_password

def hello_world(request):
    return HttpResponse("Hello, world!")

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if UserDetails.objects.filter(email=email).exists():
            return HttpResponse("Email already exists. Try logging in.")

        user = UserDetails(username=username, email=email, password=password)
        user.save()
        return redirect("login")  # Redirect to login page after signup

    return render(request, "signup.html")  # Render signup form


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = UserDetails.objects.get(email=email)
            if check_password(password, user.password):  # Secure password check
                request.session["user_id"] = user.username
                return HttpResponse(f"Welcome, {user.username}! <a href='/loginify/logout/'>Logout</a>")
            else:
                return HttpResponse("Invalid credentials, try again.")
        except UserDetails.DoesNotExist:
            return HttpResponse("Invalid credentials, try again.")

    return render(request, "login.html")

def logout(request):
    request.session.flush()
    return redirect("/loginify/login/")

def get_all_users(request):
    users = UserDetails.objects.all().values()
    return JsonResponse(list(users), safe=False) 

def get_user_by_email(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        return JsonResponse({"username": user.username, "email": user.email})
    except UserDetails.DoesNotExist:
        return HttpResponse("User not found", status=404)

def update_user(request, email):
    if request.method == "POST":
        try:
            user = UserDetails.objects.get(email=email)
            new_username = request.POST.get("username")
            new_password = request.POST.get("password")

            user.username = new_username if new_username else user.username
            user.password = new_password if new_password else user.password
            user.save()

            return HttpResponse("User updated successfully!")
        except UserDetails.DoesNotExist:
            return HttpResponse("User not found", status=404)

def delete_user(request, email):
    try:
        user = UserDetails.objects.get(email=email)
        user.delete()
        return HttpResponse("User deleted successfully!")
    except UserDetails.DoesNotExist:
        return HttpResponse("User not found", status=404)

        
