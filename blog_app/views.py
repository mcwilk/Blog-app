from django.shortcuts import render
from django.utils import timezone
from .models import Post

def index(request):
    post_list = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:3]
    unique_years = sorted([d.year for d in Post.objects.all().datetimes('publication_date', 'year')], reverse=True)
    return render(request, 'blog_app/index.html', {'post_list': post_list, 'unique_years': unique_years})



