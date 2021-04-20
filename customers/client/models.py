from django.db import models


class Telefone(models.Model):
    ddd = models.CharField(max_length=2)
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=3, choices=[('COM', ('Comercial')), ('CEL', ('Celular')), ('RES', ('Residencial'))])


class Email(models.Model):

    email = models.EmailField(max_length=240)



class Client(models.Model):

    genero = [('M', ('Masculino')), ('F', ('Feminino')), ('A', ('Agenero')), ('O', ("Outro"))]
    nome = models.CharField(max_length=70)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(unique=True, max_length=11)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=10, choices=genero)
    Telefones = models.ManyToManyField(Telefone)
    Email = models.OneToOneField(Email, on_delete=models.CASCADE)

