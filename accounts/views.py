from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2 and len(password1) >= 4:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password1
                    )

                    user.save()
                    messages.success(request, "You're now register!")
                    return redirect('login')
                else:
                    messages.error(request, "This email is taken!")
                    return redirect('register')
            else:
                messages.error(request, "This username is already in use!")
                return redirect('register')
        else:
            messages.error(request, "Passwords not match!")
            return redirect('register')
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(
            username=username,
            password=password
        )

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now log in!")
            return redirect('home')

        messages.error(request, "Incorrect pass or username!")
        return redirect('login')

    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
