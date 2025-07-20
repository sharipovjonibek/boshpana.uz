from django.db import models
from django.contrib.auth.models import User

class Rental(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Kvartira'),
        ('house', 'Uy'),
        ('studio', 'Studio'),
        ('penthouse', 'Penthouse'),
    ]
    
    CITIES = [
        ('tashkent', 'Toshkent'),
        ('samarkand', 'Samarqand'),
        ('bukhara', 'Buxoro'),
        ('andijan', 'Andijon'),
        ('namangan', 'Namangan'),
        ('fergana', 'Farg\'ona'),
        ('navoiy', 'Navoiy'),
        ('kashkadarya', 'Qashqadaryo'),
        ('surkhandarya', 'Surxondaryo'),
        ('sirdarya', 'Sirdaryo'),
        ('jizzakh', 'Jizzax'),
        ('tashkent_region', 'Toshkent viloyati'),
        ('xorezm', 'Xorazm'),
        ('karakalpakstan', 'Qoraqalpog\'iston'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, verbose_name="Uy turi")
    city = models.CharField(max_length=20, choices=CITIES, verbose_name="Shahar")
    district = models.CharField(max_length=100, verbose_name="Tuman")
    address = models.CharField(max_length=200, verbose_name="Manzil")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narx (so'm)")
    rooms = models.PositiveIntegerField(verbose_name="Xonalar soni")
    area = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Maydon (m²)")
    floor = models.PositiveIntegerField(verbose_name="Qavat")
    total_floors = models.PositiveIntegerField(verbose_name="Jami qavatlar")
    
    # Qulayliklar
    has_balcony = models.BooleanField(default=False, verbose_name="Balkon")
    has_parking = models.BooleanField(default=False, verbose_name="Avtomobil to'xtash joyi")
    has_elevator = models.BooleanField(default=False, verbose_name="Lift")
    has_air_conditioning = models.BooleanField(default=False, verbose_name="Konditsioner")
    has_internet = models.BooleanField(default=False, verbose_name="Internet")
    has_furniture = models.BooleanField(default=False, verbose_name="Mebel")
    
    # E'lon ma'lumotlari
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Egasi")
    verified = models.BooleanField(default=False, verbose_name="Tasdiqlangan")
    is_active = models.BooleanField(default=True, verbose_name="Faol")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan sana")
    
    class Meta:
        verbose_name = "Ijara uyi"
        verbose_name_plural = "Ijara uylar"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.city}"

class RentalImage(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE, related_name='images', verbose_name="Ijara uyi")
    image = models.ImageField(upload_to='rentals/', verbose_name="Rasm")
    is_primary = models.BooleanField(default=False, verbose_name="Asosiy rasm")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan sana")
    
    class Meta:
        verbose_name = "Ijara uyi rasmi"
        verbose_name_plural = "Ijara uyi rasmlari"
    
    def __str__(self):
        return f"{self.rental.title} - rasm"

class Listing(models.Model):
    property_name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    description = models.TextField()
    property_image = models.ImageField(upload_to='rentals/')
    owner_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    passport = models.CharField(max_length=20)
    cadastral_number = models.CharField(max_length=50, blank=True, null=True)
    cadastral_document = models.FileField(upload_to='cadastral_docs/', blank=True, null=True)
    card_number = models.CharField(max_length=19)
    expiry_date = models.CharField(max_length=5)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.property_name
