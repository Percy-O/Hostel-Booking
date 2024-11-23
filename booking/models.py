from django.db import models
from accounts.models import User

# Create your models here.


class Building(models.Model):
	name = models.CharField(max_length=255)
	all_rooms = models.CharField(max_length=255,null=True)
	room = models.ManyToManyField('Room')

	def __str__(self):

		return '%s'%(self.name)

class Room(models.Model):
	room_no = models.CharField(max_length=255)
	all_beds = models.CharField(max_length=255,null=True)
	bed = models.ManyToManyField('Bed')

	def __str__(self):

		return '%s'%(self.room_no)

class Bed(models.Model):
	bed_no = models.CharField(max_length=255)

	def __str__(self):

		return '%s'%(self.bed_no)

class BookHostel(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	building = models.ForeignKey(Building,on_delete=models.CASCADE)
	room = models.ForeignKey(Room,on_delete=models.CASCADE)
	bed = models.ForeignKey(Bed,on_delete=models.CASCADE)
	booked = models.BooleanField(default=False)

	def __str__(self):
		return str(self.user)





