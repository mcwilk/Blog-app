from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render 
from django.utils import timezone
from .models import Post, Comment
from .forms import PostSheet, SignupForm, CommentForm

def index(request):
    post_list = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:5]
    unique_years = sorted([d.year for d in Post.objects.all().datetimes('publication_date', 'year')], reverse=True)
    return render(request, 'blog_app/index.html', {'post_list': post_list, 'unique_years': unique_years})

def details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.counter += 1
    post.save()
    comments_list = post.comments.all().order_by('-created_on')
    #sort_comments_asc = post.comments.all().order_by('created_on')
    
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('details', pk=post.pk)
    
    else:
        form = CommentForm()
    
    return render(request, 'blog_app/details.html', {'post': post, 'comments_list':comments_list, 'form': form})

@login_required
def post_add(request):
    if request.method == "POST":
        form = PostSheet(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_drafts')
    
    else:
        form = PostSheet()

    return render(request, 'blog_app/post_edition.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostSheet(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('details', pk=pk)
    
    else:
        form = PostSheet(instance=post)

    return render(request, 'blog_app/post_edition.html', {'form': form, 'post': post})

@login_required
def post_drafts(request):
    posts = Post.objects.filter(publication_date__isnull=True).order_by('-creation_date')
    return render(request, 'blog_app/drafts.html', {'posts': posts})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('home')

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('home')

@login_required
def draft_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_drafts')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = SignupForm()
        
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('details', pk=comment.post.pk)

def category(request, number):
    post_cat_list = (Post.objects.filter(category1=number) | Post.objects.filter(category2=number) | Post.objects.filter(category3=number)).order_by('-publication_date')
    cat_name = Post.CATEGORIES[number - 1][1]
    return render(request, 'blog_app/category.html', {'post_cat_list': post_cat_list, 'cat_name': cat_name})

def archive(request):
    unique_years = sorted([d.year for d in Post.objects.all().datetimes('publication_date', 'year')], reverse=True)
    return render(request, 'blog_app/archive.html', {'unique_years': unique_years})

def archive_list(request, year):
    post_year_list = Post.objects.filter(publication_date__year=year)
    return render(request, 'blog_app/archive_list.html', {'post_year_list': post_year_list, 'year': year})

def about(request):
    return render(request, 'blog_app/about.html')