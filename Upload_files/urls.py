'''
    In this file we will store our urls to app Upload files
'''

from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.all_posts, name='post_list'),
    path('login', views.login_page, name='login'),
    path('log_out', views.log_out, name='log_out'),
    path('register', views.register, name='register'),
    path('create_thread', views.post_create, name='create_thread'),
    path('<str:title>', views.post_detail, name='post_detail'),
    path('project+list/', views.all_posts_inherit, name='projects_list'),
    path('images_disp', views.display_images, name='images'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)