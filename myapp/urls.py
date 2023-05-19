from django.urls import path, include
from django.contrib.auth import views as auth_views
from myapp.views import main, description, watch_blog, comments, create, publication_update, publication_delete, \
    profile, registration, logout_view, change_data, post_list


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('register/', registration, name='register'),
    path('register/change_password/', change_data, name='change'),
    path('login/', auth_views.LoginView.as_view(template_name='navigations/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('blogs/', post_list, name='blogs'),
    path('about/', description, name='site_description'),
    path('<slug:post_slug>/', watch_blog, name='post'),
    path('<slug:comment>/', comments, name='comment'),
    path('blogs/create/', create, name='create'),
    path('<slug:slug>/update/', publication_update, name='publication_update'),
    path('<slug:slug>/delete/', publication_delete, name='publication_delete'),
    path('profile//<str:username>', profile, name='profile'),



]