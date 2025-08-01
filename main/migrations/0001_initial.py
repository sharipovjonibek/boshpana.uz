# Generated by Django 5.1.6 on 2025-07-18 22:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Sarlavha')),
                ('description', models.TextField(verbose_name='Tavsif')),
                ('property_type', models.CharField(choices=[('apartment', 'Kvartira'), ('house', 'Uy'), ('studio', 'Studio'), ('penthouse', 'Penthouse')], max_length=20, verbose_name='Uy turi')),
                ('city', models.CharField(choices=[('tashkent', 'Toshkent'), ('samarkand', 'Samarqand'), ('bukhara', 'Buxoro'), ('andijan', 'Andijon'), ('namangan', 'Namangan'), ('fergana', "Farg'ona"), ('navoiy', 'Navoiy'), ('kashkadarya', 'Qashqadaryo'), ('surkhandarya', 'Surxondaryo'), ('sirdarya', 'Sirdaryo'), ('jizzakh', 'Jizzax'), ('tashkent_region', 'Toshkent viloyati'), ('xorezm', 'Xorazm'), ('karakalpakstan', "Qoraqalpog'iston")], max_length=20, verbose_name='Shahar')),
                ('district', models.CharField(max_length=100, verbose_name='Tuman')),
                ('address', models.CharField(max_length=200, verbose_name='Manzil')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Narx (so'm)")),
                ('rooms', models.PositiveIntegerField(verbose_name='Xonalar soni')),
                ('area', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Maydon (m²)')),
                ('floor', models.PositiveIntegerField(verbose_name='Qavat')),
                ('total_floors', models.PositiveIntegerField(verbose_name='Jami qavatlar')),
                ('has_balcony', models.BooleanField(default=False, verbose_name='Balkon')),
                ('has_parking', models.BooleanField(default=False, verbose_name="Avtomobil to'xtash joyi")),
                ('has_elevator', models.BooleanField(default=False, verbose_name='Lift')),
                ('has_air_conditioning', models.BooleanField(default=False, verbose_name='Konditsioner')),
                ('has_internet', models.BooleanField(default=False, verbose_name='Internet')),
                ('has_furniture', models.BooleanField(default=False, verbose_name='Mebel')),
                ('verified', models.BooleanField(default=False, verbose_name='Tasdiqlangan')),
                ('is_active', models.BooleanField(default=True, verbose_name='Faol')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Yangilangan sana')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Egasi')),
            ],
            options={
                'verbose_name': 'Ijara uyi',
                'verbose_name_plural': 'Ijara uylar',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ism')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefon')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('message', models.TextField(verbose_name='Xabar')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.rental', verbose_name='Ijara uyi')),
            ],
            options={
                'verbose_name': 'Aloqa',
                'verbose_name_plural': 'Aloqalar',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='RentalImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='rentals/', verbose_name='Rasm')),
                ('is_primary', models.BooleanField(default=False, verbose_name='Asosiy rasm')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Yaratilgan sana')),
                ('rental', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main.rental', verbose_name='Ijara uyi')),
            ],
            options={
                'verbose_name': 'Ijara uyi rasmi',
                'verbose_name_plural': 'Ijara uyi rasmlari',
            },
        ),
    ]
