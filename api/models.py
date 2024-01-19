from django.db import models
from rest_framework import serializers

# Create your models here.
class Programmer(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    age =models.PositiveBigIntegerField()
    is_active = models.BooleanField(default=True)
    

class UserDTO:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

class Subjet:
  def __init__(self, name, code):
    self.name = name
    self.code = code  


class User:
    def __init__(self,_id,username,email,password ):
        self._id = _id
        self.username = username
        self.email = email
        self.password = password
        