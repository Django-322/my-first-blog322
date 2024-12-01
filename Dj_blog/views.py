from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
#from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
#from django.shortcuts import redirect
#11111111111111111111111111111111111111111111111111111111111 выше посмотри на имп редирект
# Post.objects.get(pk=pk) problema


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Dj_blog/post_detail.html', {'post': post})
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Dj_blog/post_list.html', {'posts': posts})
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
    return render(request, 'Dj_blog/post_edit.html', {'form': form})
    #return render(request, 'Dj_blog/post_list.html', {'posts': posts})
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
    return render(request, 'Dj_blog/post_edit.html', {'form': form})
    
    #  Dj_site 1111 !!!!!! Dj_blog 1111 !!!!
