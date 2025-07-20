from django.shortcuts import render, redirect, get_object_or_404
from .models import Rental, Listing
from datetime import datetime
from .forms import ListingForm
import time
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    # Faqat faol va tasdiqlangan e'lonlarni olamiz
    rentals = Rental.objects.filter(is_active=True).select_related('owner').prefetch_related('images')
    
    # Qidiruv parametrlari
    city = request.GET.get('city')
    price_range = request.GET.get('price_range')
    
    if city:
        rentals = rentals.filter(city=city)
    
    if price_range:
        if price_range == '0-500000':
            rentals = rentals.filter(price__lte=500000)
        elif price_range == '500000-1000000':
            rentals = rentals.filter(price__gte=500000, price__lte=1000000)
        elif price_range == '1000000-2000000':
            rentals = rentals.filter(price__gte=1000000, price__lte=2000000)
        elif price_range == '2000000-5000000':
            rentals = rentals.filter(price__gte=2000000, price__lte=5000000)
        elif price_range == '5000000+':
            rentals = rentals.filter(price__gte=5000000)
    
    # Eng so'nggi 6 ta e'lonni olamiz
    rentals = rentals[:6]
    
    return render(request, 'main/home.html', {
        'rentals': rentals,
        'current_year': datetime.now().year,
        'selected_city': city,
        'selected_price_range': price_range,
    })

def search(request):
    # Barcha faol e'lonlarni olamiz
    rentals = Rental.objects.filter(is_active=True).select_related('owner').prefetch_related('images')
    
    # Qidiruv parametrlari
    city = request.GET.get('city')
    price_range = request.GET.get('price_range')
    property_type = request.GET.get('property_type')
    rooms = request.GET.get('rooms')
    
    # Filtrlarni qo'llaymiz
    if city:
        rentals = rentals.filter(city=city)
    
    if price_range:
        if price_range == '0-500000':
            rentals = rentals.filter(price__lte=500000)
        elif price_range == '500000-1000000':
            rentals = rentals.filter(price__gte=500000, price__lte=1000000)
        elif price_range == '1000000-2000000':
            rentals = rentals.filter(price__gte=1000000, price__lte=2000000)
        elif price_range == '2000000-5000000':
            rentals = rentals.filter(price__gte=2000000, price__lte=5000000)
        elif price_range == '5000000+':
            rentals = rentals.filter(price__gte=5000000)
    
    if property_type:
        rentals = rentals.filter(property_type=property_type)
    
    if rooms:
        rentals = rentals.filter(rooms=rooms)
    
    # Natijalar soni
    total_results = rentals.count()
    
    return render(request, 'main/search.html', {
        'rentals': rentals,
        'total_results': total_results,
        'selected_city': city,
        'selected_price_range': price_range,
        'selected_property_type': property_type,
        'selected_rooms': rooms,
        'current_year': datetime.now().year,
    })

def all_listings(request):
    # Barcha faol e'lonlarni olamiz
    rentals = Rental.objects.filter(is_active=True).select_related('owner').prefetch_related('images')
    
    # Qidiruv parametrlari
    city = request.GET.get('city')
    price_range = request.GET.get('price_range')
    property_type = request.GET.get('property_type')
    rooms = request.GET.get('rooms')
    
    # Filtrlarni qo'llaymiz
    if city:
        rentals = rentals.filter(city=city)
    
    if price_range:
        if price_range == '0-500000':
            rentals = rentals.filter(price__lte=500000)
        elif price_range == '500000-1000000':
            rentals = rentals.filter(price__gte=500000, price__lte=1000000)
        elif price_range == '1000000-2000000':
            rentals = rentals.filter(price__gte=1000000, price__lte=2000000)
        elif price_range == '2000000-5000000':
            rentals = rentals.filter(price__gte=2000000, price__lte=5000000)
        elif price_range == '5000000+':
            rentals = rentals.filter(price__gte=5000000)
    
    if property_type:
        rentals = rentals.filter(property_type=property_type)
    
    if rooms:
        rentals = rentals.filter(rooms=rooms)
    
    # Natijalar soni
    total_results = rentals.count()
    
    return render(request, 'main/all_listings.html', {
        'rentals': rentals,
        'total_results': total_results,
        'selected_city': city,
        'selected_price_range': price_range,
        'selected_property_type': property_type,
        'selected_rooms': rooms,
        'current_year': datetime.now().year,
    })

def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save()
            request.session['listing_id'] = listing.id
            return redirect('listing_confirm')
    else:
        form = ListingForm()
    return render(request, 'main/add_listing.html', {'form': form})


def listing_confirm(request):
    # 2-bosqich: tasdiqlash sahifasi
    listing_id = request.session.get('listing_id')
    if not listing_id:
        return redirect('add_listing')
    return render(request, 'main/listing_confirm.html', {'listing_id': listing_id})

def about_us(request):
    return render(request, 'main/about.html')

def premium(request):
    return render(request, 'main/premium.html')

def listing_detail(request, pk):
    listing = get_object_or_404(Rental, pk=pk)
    formatted_price = "{:,}".format(listing.price)
    # Asosiy rasm (RentalImage modelidan)
    main_image = None
    if hasattr(listing, 'images') and listing.images.exists():
        main_image = listing.images.first().image.url
    return render(request, 'main/listing_detail.html', {
        'listing': listing,
        'formatted_price': formatted_price,
        'main_image': main_image
    })
