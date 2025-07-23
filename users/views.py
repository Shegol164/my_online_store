from django.shortcuts import render, redirect
from .forms import UserRegisterForm  # Используем кастомную форму

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')  # Используем namespace
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
