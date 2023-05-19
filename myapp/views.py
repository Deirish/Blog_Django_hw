from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model, authenticate, login, logout
from myapp.models import Post, Comment
from myapp.forms import CommentForm, UserCreateForm, UserUpdateForm, ProfileUpdateForm



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
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'navigations/registration.html', {'form': form})

@login_required
def profile(request, user):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Профиль успешно обновлен.')
            return redirect('profile')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'navigations/registration_done.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


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


def comments(request, year, month, day, comment):
    post = get_object_or_404(Post, slug=comment,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comment.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = comment
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'watch_blog.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


def create(request):
    # if request.method == 'GET':
    #     return render(request, 'create_blog.html')
    # else:

    return render(request, 'create_blog.html')


def publication_update(request, slug=None):
    return HttpResponse("Update publication")


def publication_delete(request, slug=None):
    return HttpResponse("Delete publication")

