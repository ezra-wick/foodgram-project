from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm, PasswordChangingForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from django.shortcuts import render, redirect

class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'reg.html'
    success_message = "Создан новый профиль!"
    

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			messages.info(request, 'Логин или пароль неправильные')
	form_class = CreationForm
	context = {'form':form_class}
	return render(request, 'authForm.html', context)

def logoutPage(request):
    logout(request)
    return redirect('index')

class PasswordChangeView(PasswordChangeView):    
    form_class = PasswordChangingForm
    success_message = 'Получилось!'
    success_url = reverse_lazy('index')
