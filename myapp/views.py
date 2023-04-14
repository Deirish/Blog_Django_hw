from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return HttpResponse("It's your blog page!")


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
