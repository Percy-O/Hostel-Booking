from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required



from accounts import forms,models

# Create your views here.

def studentRegister(request , *args, **kwargs):

	if request.method == 'POST':
		registered =False
		form = forms.UserForm(data=request.POST)
		if form.is_valid():
			form.save(commit=True)
			registered =True
			if registered == True:
		 		messages.success(request,'Account Successfully Created!')
		 		return redirect('login')

			# if 'avatar' in request.FILES:
			# 	form.avatar = request.FILES['avatar']
			# 	form.save()
			# 	registered =True
			# 	if registered == True:

			# 		messages.success(request,'Account Successfully Created!')
			# 		return redirect('login')
			# 	else:
			# 		messages.success(request,'Unable To Save Account!')
			# else:

			# 	messages.error(request,'Image File is Invalid!')
		else:

			messages.error(request,'Unable To Save Form!')
	else:

		form = forms.UserForm()

	context={'form':form}
	return render(request,'accounts/register.html',context)


def studentLogin(request, *args, **kwargs):

	if request.method == 'POST':

		username = request.POST.get('username')
		password = request.POST.get('password')

		try:
			models.User.objects.get(username=username)
		except:
			messages.error(request,'User Not Exist!')
		else:
			
			user = authenticate(request,username=username,password=password)

			if user is not None:

				login(request,user)
				return redirect('dashboard')

			else:

				messages.error(request,'Username And Password Is Not Valid')
	context={}
	return render(request,'accounts/login.html',context)


def studentLogout(request):

	logout(request)
	return redirect('home')