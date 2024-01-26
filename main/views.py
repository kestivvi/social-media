from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, PostForm, CommentForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout
from .models import Post, Comment
from django.contrib.auth.models import Permission
from django.http import JsonResponse


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()

    i = len(posts)-1
    tmp = []
    while i >= 0:
        tmp.append(posts[i])
        i -= 1
    posts = tmp

    for p in posts:
        p.description = p.description.split("\r\n")
    for c in comments:
        c.description = c.description.split("\n")


    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")
        comment_id = request.POST.get("comment-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (
                post.author == request.user or request.user.has_perm("main.delete_post")
            ):
                post.delete()
        elif user_id:
            user = get_user_model().objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name="default")
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name="mod")
                    group.user_set.remove(user)
                except:
                    pass
        elif comment_id:
            comment = Comment.objects.filter(id=comment_id).first()
            if Comment and (
                comment.author == request.user or request.user.has_perm("main.delete_comment")
            ):
                comment.delete()

    return render(request, "main/home.html", {"posts": posts, "comments": comments})


@login_required(login_url="/login")
@permission_required("main.add_post", login_url="/login", raise_exception=True)
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()

    return render(request, "main/create_post.html", {"form": form})

@login_required(login_url="/login")
@permission_required("main.add_post", login_url="/login", raise_exception=True)
def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post=post)

    post.description = post.description.split("\r\n")
    for c in comments:
        c.description = c.description.split("\n")

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("/home")  # Możesz dostosować ścieżkę przekierowania

    else:
        form = CommentForm()

    return render(request, "main/add_comment.html", {"form": form, "post": post, "comments": comments})

@login_required(login_url="/login")
@permission_required("main.add_post", login_url="/login", raise_exception=True)
def modify_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    oryginal_val = {'title': post.title, 'description': post.description}

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = request.POST.get('title', '')
            post.description = request.POST.get('description', '')
            post.save()
            return redirect("/home")
    else:
        form = PostForm(initial=oryginal_val)

    return render(request, "main/modify_post.html", {"form": form, "post": post})

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.user_permissions.add(Permission.objects.get(codename="add_post"))
            login(request, user)
            return redirect("/home")
    else:
        form = RegisterForm()

    return render(request, "registration/sign_up.html", {"form": form})
