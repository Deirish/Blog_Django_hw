from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from myapp.models import Post, Comment
from myapp.forms import CommentForm, UserCreateForm


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
        user_form = UserCreateForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'navigations/registration_done.html', {'new_user': new_user})
    else:
        user_form = UserCreateForm()
        return render(request, 'navigations/registration.html', {'user_form': user_form})


def login(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = UserCreateForm()
    return render(request, 'navigations/login.html', {'form': form})


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
    return render(request, 'create_blog.html')


def publication_update(request, slug=None):
    return HttpResponse("Update publication")


def publication_delete(request, slug=None):
    return HttpResponse("Delete publication")


def profile(request, username=None):
    return HttpResponse("This is the user's personal page")
