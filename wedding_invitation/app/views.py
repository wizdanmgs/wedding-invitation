from django.shortcuts import render
from .models import Message


def index(request):
    to = request.GET.get("to")
    context = {
        "to": to,
        "messages": Message.objects.all(),
    }
    return render(request, "index.html", context)
