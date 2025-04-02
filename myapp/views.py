import json  # andles JSON request parsing
from django.http import JsonResponse  #Sends JSON responses
from django.shortcuts import render, redirect  #import For rendering templates and redirections
from django.views.decorators.csrf import csrf_exempt  #Disables CSRF for testing purposes
from django.contrib.auth.hashers import make_password, check_password  #import for Secure password handling
from .models import User  #Importing the MongoDB User model
import openai
import os



@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")
            openai.api_key=os.getenv("OPENAI_API_KEY")


            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a drug information chatbot trained to provide reliable, evidence-based information about medications and interactions with other substances. Always clarify that users should consult a healthcare provider before making any medical decisions. Respond clearly and concisely, and do not provide personal medical advice."
                    },
                    {"role": "user", "content": user_message}
                ]
            )
            


            bot_reply = response.choices[0].message.content
            return JsonResponse({"response": bot_reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)

def index(request):
    #Renders the index page which contains the login/register forms
    return render(request, "index.html")


@csrf_exempt
def register_user(request):
    #Handles user registration.
    if request.method == "POST":
        try:
            #Parses JSON request data
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            #Checks if username already exists in MongoDB
            if User.objects.filter(username=username).exists():
                return JsonResponse({"error": "Username already exists"}, status=400)

            #Creates and saves new user (password is automatically hashed in the model)
            user = User(username=username, password=password)
            user.save()

            return JsonResponse({"message": "User registered successfully!"})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)  #Returns any errors


@csrf_exempt
def login_user(request):
    #Handles user login authentication.
    if request.method == "POST":
        try:
            #Parses JSON request data
            data = json.loads(request.body)
            username = data.get("username")
            password = data.get("password")

            #Checks if user exists in the MongoDB database
            user = User.objects.filter(username=username).first()

            if user and user.check_password(password):  # Validates the password
                return JsonResponse({"message": "Login successful!", "redirect": "/chat/"})  # Redirects to chat page
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=401)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)  # Returns any errors


def chat_page(request):
    #Renders the chat page after login.
    return render(request, "chat.html")  #Ensures chat.html exists in your templates folder
