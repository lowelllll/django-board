from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save();
            messages.success(request, '회원가입에 성공했습니다.')
            return redirect(settings.LOGIN_URL)
    else:
        form = SignupForm()
    return render(request, 'registration/signup_form.html', {'form':form})