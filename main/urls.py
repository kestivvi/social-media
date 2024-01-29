from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("sign-up", views.sign_up, name="sign_up"),
    path("create-post", views.create_post, name="create_post"),
    path("logout/", logout_view, name="logout"),
    path('create_comment/<int:post_id>/', views.create_comment, name='create_comment'),
    path('modify-post/<int:post_id>/', views.modify_post, name='modify_post'),
    path('modify-comment/<int:comment_id>/', views.modify_comment, name='modify_comment'),
]
