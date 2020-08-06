from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Fav
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def privacypolicy(request):
    return render(request,'privacypolicy.html')


def adoption(request):
    return render(request,'home.html')

def favorite(request):
    favs = Fav.objects
    return render(request, 'pets/favorite.html',{'favs':favs})

@csrf_exempt
@login_required(login_url="/accounts/login")
def create(request):
	if request.method == 'POST':
		if request.POST['fav_name'] and request.POST['fav_age'] and request.POST['fav_breed'] and request.POST['fav_url'] and request.POST['fav_image']:
			fav = Fav()
			fav.fav_name = request.POST['fav_name']
			fav.fav_age = request.POST['fav_age']
			fav.fav_breed = request.POST['fav_breed']
			fav.fav_url = request.POST['fav_url']
			fav.fav_image = request.POST['fav_image']
			fav.user_key = request.user
			fav.save()
			return redirect('pets' )
		else:
			return render(request, 'home.html',{'error':'Error Nothing Added .'})
	else:
		return render(request, 'home.html')
