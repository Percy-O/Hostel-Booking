from django.urls import path
from booking import views

urlpatterns=[

		path('dashboard/',views.dashboard,name='dashboard'),
		path('hostel/buildings/',views.building,name='building'),
		path('hostel/buildings/<int:pk>/room/',views.getRoom,name='get_room'),
		path('hostel/buildings/room/<int:pk>/bed/',views.getBed,name='get_bed'),
		path('hostel/book/<int:pk>/',views.bookHostel,name='bookhostel'),
		path('hostel/generate/information/',views.generateData,name='generate'),
		path('hostel/generate/receipt/',views.generateReceipt,name='generate_receipt'),

]