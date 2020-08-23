from django.shortcuts import render, redirect
from .scripts.getIP import getIP
from .models import Post
from .forms import PostForm

def ip_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, 'IPapp/ip_site.html', {'ip': getIP(), 'posts': Post.objects.all().order_by('-id'), 'form': form})

