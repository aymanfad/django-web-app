from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing
from django.core.mail import send_mail
from django.shortcuts import redirect
from listings.forms import BandForm, ContactUsForm

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def about(request):
    return HttpResponse(request, '<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    listing = Listing.objects.all()
    return render(request, 'listings/list.html', {'listings':listing})



    
def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
            )
        return redirect('https://en.wikipedia.org/wiki/Main_Page')
    else:
        form = ContactUsForm()
    
    return render(request, 'listings/contact.html', {'form':form})



def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,'listings/band_detail.html',{'band': band})


def listing_detail(request, list_id):
    listing = Listing.objects.get(id=list_id)
    return render (request,'Listings/listing_detail.html',{'listing':listing})


def band_create(request):
   form = BandForm()
   return render(request,'listings/band_create.html',{'form': form})






