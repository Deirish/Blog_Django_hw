from django.urls import path, include
from myapp.views import main, description, watch_blog, comment, create, publication_update, publication_delete, \
    profile, registration, login, logout, change_data


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('register/', registration, name='register'),
    path('register/change_password/', change_data, name='change'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('blogs/', main, name='blogs'),
    path('about/', description, name='site_description'),
    path('<slug:slug>/', watch_blog, name='look_blog'),
    path('<slug:slug>/comment/', comment, name='comment'),
    path('blogs/create/', create, name='create'),
    path('<slug:slug>/update/', publication_update, name='publication_update'),
    path('<slug:slug>/delete/', publication_delete, name='publication_delete'),
    path('profile/<str:username>/', profile, name='profile'),



]