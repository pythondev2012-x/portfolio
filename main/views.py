from django.shortcuts import render
from .models import About, Project


def index(request):
    about = About.objects.first()
    projects = Project.objects.all()

    context = {
        "about": about,
        "projects": projects
    }

    return render(request, "index.html", context)