from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('post/drafts', views.post_drafts_list, name='post_drafts_list'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    path('^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
] 