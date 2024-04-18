from django.contrib.auth.models import BaseUserManager

class UsuarioManage(BaseUserManager):
    
    def create_user(self, correo, password=None, **kwargs):
        
        if not correo:
            raise ValueError("el correo es obligatorio")
        
        correo = self.normalize_email(correo)
        usuario = self.model(correo=correo, **kwargs)
        
        if password:
           usuario.set_password(password)
           
        else:
            raise ValueError("contraseña obligatoria")
            
        usuario.save(using=self._db)
        
        return usuario
    
    
    def create_superuser(self, correo, password=None, **kwargs):
        
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        
        if kwargs.get('is_staff') is not True:
            raise ValueError("Superusuario must have is_staff=true ")
        if kwargs.get('is_superuser') is not True:
           raise ValueError("Superuser must have is_superuser=true")
       
        return self.create_user(correo,password, **kwargs)
            
        