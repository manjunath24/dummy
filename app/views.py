from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

import random

from .models import Institute, InstituteActivation
from .forms import InstituteRegForm
from .service import UserService


def sign_up(request):
	form = InstituteRegForm()
	if request.method == 'POST':
		form = InstituteRegForm(request.POST)
		if form.is_valid():
			institute = form.save()
			activation = InstituteActivation(institute=institute, activation_code=random.randrange(10000,90000 , 2))
			activation.save()
			send_mail = UserService(institute.email, activation.activation_code)
			send_mail.send_activation_link()
			redirect('institute_registration')
	context = {'form': form}
	return render(request, 'registration.html', context)


def confirm_signup(request):
    user = request.GET.get('user')	
    try:
    	confirm = InstituteActivation.objects.get(activation_code=user)
    except InstituteActivation.DoesNotExist:
    	print 'Invalid confirmation'
    else:
        confirm.institute.is_active = True
        confirm.institute.save()
    return render(request, 'success.html')
