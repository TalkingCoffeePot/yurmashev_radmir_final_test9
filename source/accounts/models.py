from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Profile(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    avatar  = models.ImageField('Аватар', upload_to='user_pics')
    name = models.CharField('Имя', max_length=100, blank=True, null=True)
    info = models.TextField('Инфо', max_length=1000, blank=True, null=True)
    number = models.IntegerField('Номер телефона', blank=True, null=True)
    subs = models.ManyToManyField('Profile', blank=True, null=True, related_name='my_subs')
    sex = models.CharField('Пол', max_length=1, blank=False, null=True, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        return self.username
    
