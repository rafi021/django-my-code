from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('post-list/', views.post_list, name='post-list'),
    re_path(r'^single-post/(?P<post_id>[0-9]+)/', views.single_post, name='single-post'),

]