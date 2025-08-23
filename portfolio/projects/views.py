from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project
from twilio.rest import Client

def home(request):
    projects = Project.objects.all()
    return render(request, "projects/home.html", {"projects": projects})


def hire_me(request):
    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        if not email or not message:
            messages.error(request, "Please provide both email and message.")
            return redirect("home")

        body = f"Hire request from {email}\n\n{message}"

        # Twilio credentials (put in settings or env vars later)
        account_sid = "AC7eb2031efb05262e155ad13f1b65a889"
        auth_token = "4a14cd5c9fe4085a014b81e460ced711"
        client = Client(account_sid, auth_token)

        try:
            client.messages.create(
                from_="whatsapp:+14155238886", # Twilio sandbox number
                body=body,
                to="whatsapp:+919060211542"  # your WhatsApp number (with country code)
            )
            messages.success(
            request,
            "Thankyou for your interest. I will reply asap from amitinger25@gmail.com"
            )
        except Exception as e:
            messages.error(request, f"Could not send WhatsApp: {e}")

        return redirect("home")
