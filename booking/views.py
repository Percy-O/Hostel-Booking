from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from booking import models,forms

from fpdf import FPDF
from django.http import FileResponse

# Create your views here.


def dashboard(request):

	buildings = models.Building.objects.all()

	context={'buildings':buildings}
	return render(request,'booking/dashboard.html',context)


def building(request,*args,**kwargs):

	get_bed=None
	# All building
	buildings = models.Building.objects.all()
	for building in buildings:
		for room in building.room.all():
			get_bed = room.all_beds
	context={'buildings':buildings,'get_bed':get_bed}
	return render(request,'booking/buildings.html',context)

def getRoom(request,pk):
	view_bed= False

	building= models.Building.objects.get(id=pk)

	request.session['building'] = building.name
	# All Rooms
	rooms = building.room.all()

	# view_bed = True
	# # Get Room
	# room = models.Room.objects.get(id=pk)

	# request.session['room'] = room.room_no
	# # Get All Beds
	# beds= room.bed.all()




	context={
		'building':building,
		'rooms':rooms,
		'view_bed':view_bed,
		}

	return render(request,'booking/room_bed.html',context)

def getBed(request,pk):

	view_bed = True
	# Getting Building
	get_building = request.session.get('building')
	building = models.Building.objects.get(name=get_building)

	# Filter Room
	rooms = models.Room.objects.filter(id=pk)

	# Get Room
	room = models.Room.objects.get(id=pk)

	request.session['room'] = room.room_no
	# Get All Beds
	beds= room.bed.all()

	context = {
		'room':room,
		'beds':beds,
		'rooms':rooms,
		'view_bed':view_bed,
		'building':building,
	}

	return render(request,'booking/room_bed.html',context)


def bookHostel(request,pk):
	# Building Session
	get_building_session = request.session.get('building')

	# Room Session
	get_room_session = request.session.get('room')

	# Get Bed Through Keyword
	get_bed_kwarg = models.Bed.objects.get(pk=pk)

	if request.method == 'POST':
	
		get_building = request.POST.get('building')
		building = models.Building.objects.get(name=get_building)
		
		get_room = request.POST.get('room')
		room = models.Room.objects.get(room_no=get_room)

		get_bed = request.POST.get('bed')
		bed = models.Bed.objects.get(bed_no=get_bed)

		try:
			user = models.BookHostel.objects.get(user=request.user)
		
		except:

			try:
				form = models.BookHostel.objects.create(

						user = request.user,
						building = building,
						room= room,
						bed = bed,
						booked = True
					).save()
			except:
				messages.error(request,f'UNABLE TO BOOK ROOM {get_room_session}')
			else:
				messages.success(request,f'ROOM "{get_room_session}" SUCCESSFULLY BOOKED')

				# Remove Bed Being Booked By User
				room = models.Room.objects.get(room_no=get_room_session)
				# Getting Bed identity
				bed = models.Bed.objects.get(pk=pk)
				# Remove Bed
				remove_bed = room.bed.remove(bed)

				return redirect('generate')
		
		else:
			messages.error(request,f" You Have Already Booked In Hostel")
		

	context = {
		'building':get_building_session,
		'room':get_room_session,
		'bed':get_bed_kwarg,
		}
	return render(request,'booking/bookhostel.html',context)


def generateData(request):

	# User Hostel Data Beign Booked
	user_book = models.BookHostel.objects.get(user=request.user)

	context={'user':user_book}

	return render(request,'booking/generate.html',context)


def generateReceipt(request):

	title ='OYO STATE COLLEGE OF AGRICULTURE AND TECHNOLOGY,IGBOORA'
	class PDF(FPDF):

		def header(self):
			# Logo
			self.image('./static/images/oyscatech.jpeg',10,8,25)
			# Font
			self.set_font('times','B',15)
			self.set_text_color(7,69,38)
			# Padding
			self.cell(20)
			
			# Title
			self.multi_cell(0,10,'OYO STATE COLLEGE OF AGRICULTURE AND TECHNOLOGY,IGBOORA,OYO STATE',border=False,ln=True, align='C')
			
			self.set_font('helvetica','I',8)
			self.set_text_color(0,0,0)
			self.cell(20)
			self.cell(0,4,'INNOVATION,FOOD SUFFICIENCY,SELF EMPLOYMENT',border=False,align='C')
			
			self.dashed_line(10,35,200,35,dash_length=1,space_length=1)
			
			# line break
			self.ln(10)

		def footer(self):
			# Set Position of the footer

			self.set_y(-15)
			# Set font

			self.set_font('helvetica','I',10)
			
			# Set line
			self.dashed_line(10,284,200,284, dash_length=1, space_length=1) # 300 height , width >200
			# self.line(10,280,200,280)
			
			# Page Number
			self.cell(0,10,f'Page{self.page_no()}/{{nb}}',align='C')


	# Create An Objedct
	# Layout ('P','L')
	# Unit ('mm','cm','in') millimeter ,centimeter ,inch
	# format ('A3','A4',(default),'A5','letter','legal',(100,150))

	hostel= models.BookHostel.objects.get(user=request.user)


	pdf = PDF('P','mm','A4')

	# get the total page number
	pdf.alias_nb_pages()

	# Create Metadata
	pdf.set_title('Oyscatech Hostel Receipt')
	pdf.set_author('Oyscatech')

	# Set auto page break
	pdf.set_auto_page_break(auto=True,margin=15)

	# Add a page

	pdf.add_page()

	# Student Information
	pdf.set_font('times','B',14)
	pdf.cell(0,10,'Student Information',ln=True)
	pdf.set_font('times','',11)




	pdf.ln(1)
	pdf.set_draw_color(233,236,239)
	# Image 
	image = pdf.image(f'.{hostel.user.avatar.url}',172,52,25)

	# First Row
	pdf.set_font('times','B')
	pdf.cell(20,13,'Full Name:',border=1,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(50,13,hostel.user.name,border=1,ln=0,align='L',)
	pdf.set_font('times','B')
	pdf.cell(30,13,'Email Address:',border=1,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(60,13,hostel.user.email,border=1,ln=1,align='L',)

	# Second Row
	pdf.set_font('times','B')
	pdf.cell(30,13,'Username:',border=1,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(40,13,f'{hostel.user.username}',border=1,ln=0,align='L',)
	pdf.set_font('times','B')
	pdf.cell(30,13,'Phone Number:',border=1,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(30,13,f'{hostel.user.phone_num}',border=1,ln=0,align='L',)
	pdf.set_font('times','B')
	pdf.cell(20,13,'Gender:',border=1,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(10,13,hostel.user.gender,border=1,ln=0,align='L',)



	pdf.ln(20)

	# Hostel Information
	pdf.set_font('times','B',14)
	pdf.cell(0,10,'Hostel Information',ln=True)
	pdf.set_font('times','',11)

	pdf.ln(1)

	# First Row
	pdf.set_font('times','B')
	pdf.cell(30,13,'Building Name:',border=1,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(20,13,hostel.building.name,border=1,ln=0,align='L',)
	pdf.set_font('times','B')
	pdf.cell(42,13,'Building Description:',border=1,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(57,13,f' Building with {hostel.building.all_rooms} rooms and {hostel.room.all_beds} beds',border=1,ln=0,align='L',)
	pdf.set_font('times','B')
	pdf.cell(23,13,'All Rooms:',border=1,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(18,13,f'{hostel.building.all_rooms} Rooms',border=1,ln=1,align='L',)

	# Second Row
	pdf.set_font('times','B')
	pdf.cell(35,13,'Room Number:',border=1,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(25,13,hostel.room.room_no,border=1,ln=0,align='L',)
	pdf.set_font('times','B')
	pdf.cell(50,13,'Total Bed Available:',border=1,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(25,13,f'{hostel.room.all_beds} beds',border=1,ln=0,align='L',)
	pdf.set_font('times','B')
	pdf.cell(35,13,'Choosen Bed:',border=1,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(20,13,f'{hostel.bed.bed_no}',border=1,ln=1,align='L',)
	
	

	pdf.set_draw_color(0,0,0)
	
# Student Signature
	pdf.set_font('','B')
	pdf.line(10,150,50,150)
	pdf.cell(40,64,hostel
.user.name,align='C')
	pdf.ln(4)
	pdf.set_font('','I')
	pdf.cell(40,65,'Student Signature',align='C')

# Bursary Signature
	pdf.set_font('','B')
	pdf.line(150,150,190,150)
	pdf.cell(70)
	pdf.cell(100,55,'Bursary',align='C')
	pdf.ln(4)
	pdf.set_font('','I')
	pdf.cell(110)
	pdf.cell(100,56,'Bursary Signature',align='C')

	
	pdf.output(f'Hostel Receipt.pdf','F')
	return FileResponse(open(f'Hostel Receipt.pdf','rb'), as_attachment=False, content_type='application/pdf')




