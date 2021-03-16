from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('User Authenticated Successfully')
                else:
                    return HttpResponse('Disable Account')
            else:
                return HttpResponse('Invalid Login Credentials')
        else:
            form = LoginForm()
        return render(request,
                      'account/login.html',
                      {'form': form})
    else:
        form = LoginForm()
        return render(request,
                      'account/login.html',
                      {'form': form})
