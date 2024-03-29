from django.db import models
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .validators import quantity_validator, price_validator


class Print(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=120, help_text='Автор')
    description = models.TextField(help_text='Описание')
    image = models.ImageField(upload_to='prints/')
    quantity = models.IntegerField(default=0, validators=quantity_validator,
                                   help_text='Enter a value between 1 and 50.')
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=price_validator,
                                help_text='Enter a value between 0.02 and 99999.'
                                )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('prints:prints-detail', kwargs={'my_id': self.id})

    def __str__(self):
        return self.title


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prints = models.ManyToManyField(Print, through='CartPrint')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartPrint(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    print = models.ForeignKey(Print, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, validators=quantity_validator,
                                   help_text='Enter a value between 1 and 50.')

    def __str__(self):
        return f'{self.pk} {self.print.title} - {self.cart.user}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)