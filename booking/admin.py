from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html,urlencode
from django.db.models import Count
from booking import models

# Register your models here.

@admin.register(models.Building)
class BuildingAdmin(admin.ModelAdmin):
	list_display = ['id','name','all_rooms','room_posted']
	search_fields = ['name']


	def room_posted(self,building):

		url_link = (
			reverse('admin:booking_room_changelist')
			+ '?'
			+ urlencode({
					'building__id':str(building.id)
				})
			)
		rooms = format_html('<a href="{}">{}</a>',url_link,f'{building.rooms_posted} Rooms')
		return rooms

	def get_queryset(self,request):
		room_count = super().get_queryset(request).annotate(rooms_posted=Count('room'))
		return room_count

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
	list_display = ['id','room_no','bed_available']

	def bed_available(self,room):
		url_link = (
			reverse('admin:booking_bed_changelist')
			+ '?'
			+ urlencode({
				'room__id':str(room.id)
				})
			)

		all_bed = (format_html('<a href="{}">{}</a>',url_link,f'{room.all_bed} Beds'))
		return all_bed

	def get_queryset(self,request):
		all_bed = super().get_queryset(request).annotate(all_bed=Count('bed'))
		return all_bed

@admin.register(models.Bed)
class BedAdmin(admin.ModelAdmin):
	list_display = ['id','bed_no']

@admin.register(models.BookHostel)
class BookHostelAdmin(admin.ModelAdmin):
	list_display = ['student_name','building','room','bed','book_status']
	search_fields = ['user__first_name__istartswith','user__last_name__istartswith']

	@admin.display(ordering='student_name')
	def student_name(self,bookhostel):
		return f'{bookhostel.user.name}'

	@admin.display(ordering='book_status')
	def book_status(self,bookhostel):
		if bookhostel.booked == False:
			return 'Pending'
		else:
			return 'Booked'

