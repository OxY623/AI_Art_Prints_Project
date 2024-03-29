# Generated by Django 4.2.1 on 2023-05-28 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Название', max_length=120)),
                ('artist', models.CharField(help_text='Автор', max_length=120)),
                ('description', models.TextField(help_text='Описание')),
                ('image', models.ImageField(upload_to='prints/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
