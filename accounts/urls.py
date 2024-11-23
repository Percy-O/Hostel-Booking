from django.urls import path
from accounts import views

urlpatterns=[

	path('login/',views.studentLogin,name='login'),
	path('logout/',views.studentLogout,name='logout'),
	path('register/',views.studentRegister,name='register'),

]