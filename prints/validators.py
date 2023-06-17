from django.core.validators import MinValueValidator, MaxValueValidator

quantity_validator = [MaxValueValidator(50), MinValueValidator(1)]
price_validator = [MaxValueValidator(99999), MinValueValidator(0.02)]
price_validator = [MaxValueValidator(99999), MinValueValidator(0.02)]