from django.shortcuts import get_object_or_404, redirect, render 
from django.utils import timezone
from .models import Post
from .forms import PostSheet

def index(request):
    post_list = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:4]
    unique_years = sorted([d.year for d in Post.objects.all().datetimes('publication_date', 'year')], reverse=True)
    return render(request, 'blog_app/index.html', {'post_list': post_list, 'unique_years': unique_years})

def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_app/details.html', {'post': post})

def post_add(request):
    if request.method == "POST":
        form = PostSheet(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publication_date = timezone.now()
            post.save()
            return redirect('details', pk=post.pk)
    
    else:
        form = PostSheet()

    return render(request, 'blog_app/post_edition.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostSheet(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publication_date = timezone.now()
            post.save()
            return redirect('details', pk=post.pk)
    
    else:
        form = PostSheet(instance=post)

    return render(request, 'blog_app/post_edition.html', {'form': form, 'post': post})