from django.db import models
from django.urls import reverse


class Print(models.Model):
    title = models.CharField(max_length=120, help_text='Название')
    artist = models.CharField(max_length=120, help_text='Автор')
    description = models.TextField(help_text='Описание')
    image = models.ImageField(upload_to='prints/')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_absolute_url(self):
        return reverse('prints:prints-detail', kwargs={'my_id': self.id})

    def __str__(self):
        return self.title
