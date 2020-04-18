from django.shortcuts import render
from django.utils import timezone
from .models import Post

def index(request):
    post_list = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:5]
    last_post_id = post_list[0].id
    return render(request, 'blog_app/index.html', {'post_list': post_list, 'last_post_id': last_post_id})



