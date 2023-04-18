from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse("It's your blog page!")


def registration(request):
    return HttpResponse("It's registration page")


def login(request):
    return HttpResponse("Login page")


def logout(request):
    return HttpResponse("Logout page")


def change_data(request):
    return HttpResponse("Change personal data")


def discription(request):
    return HttpResponse("It's discription!")


def watch_blog(request, slug=None):
    data = {
        'text': slug
    }
    return HttpResponse("You can see the blog here")

def comment(request, slug=None):
    return HttpResponse("Comment")


def create(request):
    return HttpResponse("Create your post here")


def publication_update(request, slug=None):
    return HttpResponse("Update publication")


def publication_delete(request, slug=None):
    return HttpResponse("Delete publication")


def profile(request, username=None):
    return HttpResponse("This is the user's personal page")






