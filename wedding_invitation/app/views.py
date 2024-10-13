import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import Message


def index(request):
    to = request.GET.get("to")
    context = {
        "to": to,
        "messages": Message.objects.all(),
    }
    return render(request, "index.html", context)


def message(request):
    context = {}
    if request.method == "POST":
        name = request.POST["name"]
        message = request.POST["message"]
        Message.objects.create(name=name, message=message)
        context = {
            "name": name,
            "message": message,
        }

        return JsonResponse(context)
