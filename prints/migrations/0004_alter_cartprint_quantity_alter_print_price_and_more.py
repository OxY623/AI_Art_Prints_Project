
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prints', '0003_print_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartprint',
            name='quantity',
            field=models.PositiveIntegerField(default=1, help_text='Enter a value between 1 and 50.', validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='print',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='Enter a value between 0.02 and 99999.', max_digits=6, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(0.02)]),
        ),
        migrations.AlterField(
            model_name='print',
            name='quantity',
            field=models.IntegerField(default=0, help_text='Enter a value between 1 and 50.', validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(1)]),
        ),
    ]
