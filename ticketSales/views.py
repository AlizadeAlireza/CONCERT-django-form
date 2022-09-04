from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from ticketSales.models import concertModel
from django.db.models import Count
from ticketSales.models import locationModel
from ticketSales.models import timeModel
import ticketSales
from django.contrib.auth.decorators import login_required
from ticketSales.forms import ConcertForm, SearchForm
# Create your views here.

def concertlistView(request):
    concerts = concertModel.objects.all()

    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        SearchText = searchForm.cleaned_data["SearchText"]
        concerts = concertModel.objects.filter(Name__contains=SearchText)

    else:
        concerts = concertModel.objects.all()

    context = {
        "concertlist" : concerts,
        "concertcount" : concerts.count(),
        "searchForm" : searchForm
    }
    return render(request, "ticketSales/concertlist.html", context)

@login_required
def locationlistView(request):
    locations = locationModel.objects.all()
    
    context = {
        "locationlist" : locations,
        
    }
    return render(request, "ticketSales/locationlist.html", context)
    
def concertdetailsView(request,concert_id):
    concert = concertModel.objects.get(pk=concert_id)

    context = {
        "concertdetails":concert
    }

    return render(request, "ticketSales/concertdetails.html", context)

@login_required
def timeView(request):

    #if request.user.is_authenticated and request.user.is_active:

        times = timeModel.objects.all()
        
        context = {
            "timelist" : times,
            
        }
        return render(request, "ticketSales/timelist.html", context)
    #else:
        #return HttpResponseRedirect(reverse(accounts.views.loginView))

def concertEditView(request, concert_id):
    
    concert = concertModel.objects.get(pk=concert_id)

    
    if request.method=="POST":
        concertForm = ConcertForm(request.POST, request.FILES, instance = concert)
        if concertForm.is_valid():
            concertForm.save()

    
    else:
        concertForm = ConcertForm(instance = concert)

        
    context = {

            "concertForm" : concertForm,
            "PosterImage" : concert.Poster
            
        }
    return render(request, "accounts/profileRegister.html", context)  
