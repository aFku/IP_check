from django.shortcuts import render
from .scripts.getIP import getIP

# Create your views here.

def ip_view(request):
    return render(request, 'IPapp/ip_site.html', {'ip': getIP()})

