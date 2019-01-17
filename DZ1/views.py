from django.shortcuts import render
from .models import Post, Picture
from django.utils import timezone
from django.shortcuts import  render, get_object_or_404
from .forms import PostForm, PictureForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger,EmptyPage
from django.shortcuts import render_to_response
from django.template import RequestContext


def post_list(request):
    queryset_list = Post.objects.all().order_by("id")
    paginator = Paginator(queryset_list, 3)  # posts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def picture_list(request):
    queryset_list = Picture.objects.all().order_by("id")
    paginator = Paginator(queryset_list, 3)  # posts per page
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
    }
    return render(request, 'blog/picture_list.html', context)

def picture_detail(request, pk):
    picture=get_object_or_404(Picture, pk=pk)
    return render(request, 'blog/picture_detail.html', {'picture':picture})

@login_required
def picture_new(request):
    if request.method == "POST":
        form = PictureForm(request.POST)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.published_date = timezone.now()
            picture.save()
            return redirect('picture_detail', pk=picture.pk)
    else:
        form = PictureForm()
    return render(request, 'blog/picture_edit.html', {'form': form})

@login_required
def picture_edit(request, pk):
    picture = get_object_or_404(Picture, pk=pk)
    if request.method == "POST":
        form = PictureForm(request.POST, instance=picture)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.published_date = timezone.now()
            picture.save()
            return redirect('post_detail', pk=picture.pk)
    else:
        form = PictureForm(instance=picture)
    return render(request, 'blog/picture_edit.html', {'form': form})
