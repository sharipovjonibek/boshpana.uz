from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            'property_name', 'location', 'price', 'description', 'property_image',
            'owner_name', 'phone_number', 'passport', 'cadastral_number', 'cadastral_document',
            'card_number', 'expiry_date', 'zip_code'
        ]
        widgets = {
            'expiry_date': forms.TextInput(attrs={'placeholder': 'MM/YY'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '+998 90 123 45 67'}),
        } 