from django.shortcuts import render, redirect
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)  # Добавляем request.FILES
        if form.is_valid():
            user = form.save()
            # Дополнительная обработка если нужно
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

