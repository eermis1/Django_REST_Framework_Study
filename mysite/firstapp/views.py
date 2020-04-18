from actstream.models import user_stream
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the firstapp index.")

def feed(request):
    user_stream(request.user, with_user_activity=True)