from django.shortcuts import render
from fpdf import FPDF
from django.http import FileResponse
from booking.models import BookHostel
from .create_table_fpdf2 import PDF_1
# from django.shortcuts import render

def home(request):


	context={}
	return render(request,'home.html',context)

def report(request):
	title ='OYO STATE COLLEGE OF AGRICULTURE AND TECHNOLOGY,IGBOORA'
	class PDF(PDF_1):

		def header(self):
			# Logo
			self.image('./static/images/oyscatech.jpeg',10,8,25)
			# Font
			self.set_font('times','B',15)
			self.set_text_color(9,69,38)
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

	hostel= BookHostel.objects.get(user__username='Rita')

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
	pdf.set_draw_color(52,58,64)
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
	pdf.line(10,93,200,93)

	pdf.ln(1)


	pdf.set_font('times','B')
	pdf.cell(30,13,'Building Name:',border=0,ln=0,align='L')
	pdf.set_font('times','')
	pdf.cell(32,13,hostel.building.name,border=0,ln=0)

	pdf.ln(9)
	
	pdf.set_font('times','B')
	pdf.cell(36,14,'Building Description:')
	pdf.set_font('times','')
	pdf.cell(37,14,f' Building with {hostel.building.all_rooms} rooms and {hostel.room.all_beds} beds',border=0,ln=0,align='L',)

	pdf.ln(9)

	pdf.set_font('times','B')
	pdf.cell(20,15,'All Rooms:',border=0,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(20,15,f'{hostel.building.all_rooms} Rooms',border=0,ln=0,align='L',)

	pdf.ln(9)

	pdf.set_font('times','B')
	pdf.cell(27,16,'Room Number:',border=0,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(25,16,hostel.room.room_no,border=0,ln=0,align='L',)

	pdf.ln(9)

	pdf.set_font('times','B')
	pdf.cell(37,17,'Total Bed Available:',border=0,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(20,17,f'{hostel.room.all_beds} beds',border=0,ln=0,align='L',)

	pdf.ln(9)

	pdf.set_font('times','B')
	pdf.cell(30,18,'Choosen Bed:',border=0,ln=0,align='L',)
	pdf.set_font('times','')
	pdf.cell(20,18,f'{hostel.bed.bed_no}',border=0,ln=1,align='L',)

	# # First Row
	# pdf.set_font('times','B')
	# pdf.cell(30,13,'Building Name:',border=1,ln=0,align='L',)
	# pdf.set_font('times','')
	# pdf.cell(20,13,hostel.building.name,border=1,ln=0,align='L',)
	# pdf.set_font('times','B')
	# pdf.cell(42,13,'Building Description:',border=1,ln=0,align='L',)
	# pdf.set_font('times','')
	# pdf.cell(57,13,f' Building with {hostel.building.all_rooms} rooms and {hostel.room.all_beds} beds',border=1,ln=0,align='L',)
	# pdf.set_font('times','B')
	# pdf.cell(23,13,'All Rooms:',border=1,ln=0,align='L',)
	# pdf.set_font('times','')
	# pdf.cell(18,13,f'{hostel.building.all_rooms} Rooms',border=1,ln=1,align='L',)

	# # Second Row
	# pdf.set_font('times','B')
	# pdf.cell(35,13,'Room Number:',border=1,ln=0,align='L',)
	# pdf.set_font('times','')
	# pdf.cell(25,13,hostel.room.room_no,border=1,ln=0,align='L',)
	# pdf.set_font('times','B')
	# pdf.cell(50,13,'Total Bed Available:',border=1,ln=0,align='L',)
	# pdf.set_font('times','')
	# pdf.cell(25,13,f'{hostel.room.all_beds} beds',border=1,ln=0,align='L',)
	# pdf.set_font('times','B')
	# pdf.cell(35,13,'Choosen Bed:',border=1,ln=0,align='L',)
	# pdf.set_font('times','')
	# pdf.cell(20,13,f'{hostel.bed.bed_no}',border=1,ln=1,align='L',)
	

	

	
# Student Signature
	pdf.set_font('','B')
	pdf.line(10,185,50,185)
	pdf.cell(40,64,hostel.user.name,align='C')
	pdf.ln(4)
	pdf.set_font('','I')
	pdf.cell(40,65,'Student Signature',align='C')

# Bursary Signature
	pdf.set_font('','B')
	pdf.line(150,185,190,185)
	pdf.cell(70)
	pdf.cell(100,55,'Bursary',align='C')
	pdf.ln(4)
	pdf.set_font('','I')
	pdf.cell(110)
	pdf.cell(100,56,'Bursary Signature',align='C')

	
	pdf.output('report.pdf','F')
	return FileResponse(open('report.pdf','rb'), as_attachment=False, content_type='application/pdf')



