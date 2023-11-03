from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
from django.contrib.auth.hashers import make_password

# Create your models here.
class MyUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=500, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Хешируем пароль перед сохранением
        self.password = make_password(self.password)
        super(MyUser, self).save(*args, **kwargs)
>>>>>>> 343ac9a229c2342907b42270ff5d1fe137ea07e5
