from django.urls import path
from . import views
from .views import logout_view

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("sign-up", views.sign_up, name="sign_up"),
    path("create-post", views.create_post, name="create_post"),
    path("logout/", logout_view, name="logout"),
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
