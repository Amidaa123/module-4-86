from django.shortcuts import render
#from django.http import HttpResponse
from .models import Advertisement

# Create your views here.
def index(requests):
    advertisements = Advertisement.objects.all()
    context = {"advertisements": advertisements}
    return render(requests, "index.html", context=context)

def top_sellers(request):
    return render(request, "top-sellers.html")
