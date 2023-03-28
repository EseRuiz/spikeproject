from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


char_validator = RegexValidator(r"^[a-zA-Z]*", "Sólo se permiten letras.")

class Enterprise(models.Model):
    name=models.CharField(verbose_name="nombre", max_length=50,
                          validators=[char_validator])
    email=models.EmailField(verbose_name="email",max_length=150,
                            unique=True)
    phone=models.PositiveBigIntegerField(verbose_name="telefono",
                                         null=True)
    active=models.BooleanField(verbose_name="activo",default=False,
                               help_text="tramite activo")
    