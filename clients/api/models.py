from django.db import models


class Phone(models.Model):

    ddd = models.CharField(max_length=2)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=3, choices=[('COM', ('Comercial')), ('CEL', ('Celular')), ('RES', ('Residencial'))])


class Email(models.Model):

    email = models.EmailField(max_length=240)


class Client(models.Model):

    gender_spectrum = [('M', ('Male')), ('F', ('Female')), ('o', ('Other')), ('O', ("Outro"))]
    name = models.CharField(max_length=70)
    id_cart = models.CharField(max_length=20)
    social_security_number = models.CharField(unique=True, max_length=11)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_spectrum)
    Phones = models.ManyToManyField(Phone)
    Email = models.OneToOneField(Email, on_delete=models.CASCADE)