from django.db import models


class Phone(models.Model):

    channels = [('W', 'Work'),
                ('P', 'Cellphone'), ('R', 'Residential')]

    country_code = models.CharField(max_length=2)
    area_code = models.CharField(max_length=2)
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=3, choices=channels)


class Email(models.Model):

    email = models.EmailField(max_length=240)



class Client(models.Model):

    gender_spectrum = [('M', 'Male'), ('F', 'Female'),
                       ('F', ('Fluid')), ('P', ("Person"))]

    name = models.CharField(max_length=70)
    id_card = models.CharField(max_length=20)
    social_security_number = models.CharField(unique=True, max_length=11)
    birth_date = models.DateField()
    gender = models.CharField(max_length=10, choices=gender_spectrum)
    phones = models.ManyToManyField(Phone)
    email = models.OneToOneField(Email, on_delete=models.CASCADE)
