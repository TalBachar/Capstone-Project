from django.shortcuts import render
from django.views.generic import ListView

from pets.models import Pet
# Create your views here.


def home(request):
    return render(request, 'home.html', {})

class SearchView(ListView):
    model = Pet
    template_name = 'search.html'
    context_object_name = 'pets'
    paginate_by = 10

    def get_queryset(self):
       return self.model.objects.filter(title__contains=self.request.GET['q'])
