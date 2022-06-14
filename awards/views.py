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


@login_required(login_url='/accounts/login/')
def user_profile(request):
    current_user = request.user
    try:
        wasifu = Profile.objects.filter(user=current_user)[
            0:1
        ]  # wasifu is the same as profile
        user_projects = Projects.objects.filter(user=current_user)
    except Exception as e:
        raise Http404()
    if request.method == "POST":
        form = UpdateForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
        return redirect("user_profile")
    else:
        form = UpdateForm()
    return render(
        request,
        "user_profile.html",
        {"form": form, "profile": wasifu, "projects": user_projects},
    )


@login_required(login_url='/accounts/login/')
def post(request):
    current_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect("home_page")
    else:
        form = PostForm()
    return render(request, "post.html", {"form": form})
