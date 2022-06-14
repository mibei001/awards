from django.shortcuts import render, redirect
from .models import Projects, Votes, Comments, Profile
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from .forms import PostForm, CommentForm, RateForm, UpdateForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfileSerializer,  ProjectSerializer

# Create your views here.


def home_page(request):
    try:
        projects = Projects.objects.all()
    except Exception as e:
        raise Http404()
    return render(
        request, "index.html", {"projects": projects}
    )  # mradi is the same as project
