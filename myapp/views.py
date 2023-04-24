from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  myapp.models import Post, Comment
from myapp.forms import CommentForm



def main(request):
    return render(request, 'base.html')


def post_list(request):
    posts = Post.objects.filter(visible='1')
    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    querysetGoods = paginator.get_page(page)

    context = {
        'posts': posts,
        'title': "Главная страница блога",
        'desc': "Описание для главной страницы",
        'key': "ключевые, слова",
    }
    return render(request, 'home.html', context)


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


def watch_blog(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    context = {
        'post': post
    }
    return render(request, 'watch_blog.html', context)

def comment(request, slug):
    comments = get_object_or_404(Post, slug=slug)
    data = Comment.objects.filter(comments=slug)
    form = CommentForm()
    return render(request, 'watch_blog.html', {'comments': comments, 'data': data, 'form': form})


def create(request):
    return render(request, 'create_blog.html')


def publication_update(request, slug=None):
    return HttpResponse("Update publication")


def publication_delete(request, slug=None):
    return HttpResponse("Delete publication")


def profile(request, username=None):
    return HttpResponse("This is the user's personal page")






