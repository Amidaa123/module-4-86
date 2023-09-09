from django.shortcuts import render, reverse, redirect
# from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Count
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()
def index(request):
    title = request.GET.get("query")
    if title:
        advertisements = Advertisement.objects.filter(title__iexact=title)
    else:
        advertisements = Advertisement.objects.all()
    context = {"advertisements": advertisements}
    return render(request, "app_advertisement/index.html", context=context)

def top_sellers(request):
    users = User.objects.annotate(
        adv_count=Count("advertisement")
    ).order_by('-adv_count')
    context = {
        "users": users
    }
    return render(request, "app_advertisement/top-sellers.html", context)

@login_required(login_url=reverse_lazy('login'))
def advertisement_post(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {"form": form}
    return render(request, "app_advertisement/advertisement-post.html", context)

def advertisement_view(request, pk):

    advertisement = Advertisement.objects.get(pk=pk)
    context = {
        "adv": advertisement,
    }
    return render(request, "app_advertisement/advertisement.html", context)