from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'base.html')


def registration(request):
    return render(request, 'navigations/registration.html')


def login(request):
    return render(request, 'navigations/login.html')


def logout(request):
    return HttpResponse("Logout page")


def change_data(request):
    return HttpResponse("Change personal data")


def description(request):
    return HttpResponse("It's description!")


def watch_blog(request, slug=None):
    data = {
        'text': slug
    }
    return render(request, 'watch_blog.html')

def comment(request, slug=None):
    return HttpResponse("Comment")


def create(request):
    return render(request, 'create_blog.html')


def publication_update(request, slug=None):
    return HttpResponse("Update publication")


def publication_delete(request, slug=None):
    return HttpResponse("Delete publication")


def profile(request, username=None):
    return HttpResponse("This is the user's personal page")






