from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):

	GENDER_CHOICES = [
		('M','Male'),
		('F','Female')

	]
	name = models.CharField(max_length=255)
	gender = models.CharField(choices=GENDER_CHOICES,max_length=2)
	phone_num = models.IntegerField(null=True)
	avatar = models.ImageField(
		upload_to='account/image/%y-%m-%d',
		default='../static/images/avatar.jpg',
		verbose_name='Account Image',
		null=True
	)


	