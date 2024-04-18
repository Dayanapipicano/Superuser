from django.db import models
from .manages import UsuarioManage
from django.contrib.auth.models import AbstractBaseUser

class Usuario(AbstractBaseUser):
    
    user_identificacion = models.IntegerField(null=True,blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True,blank=True)
    correo = models.EmailField(unique=True)
    
    is_active = models.BooleanField("habilitado", default=True)
    is_staff = models.BooleanField("Acceso al admin", default=False)
    is_superuser = models.BooleanField("Acceso al admin", default=False)
    
    USERNAME_FIELD = 'correo'
    
    
    objects = UsuarioManage()
    