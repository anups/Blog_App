from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


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
                      'registration/login.html',
                      {'form': form})
    else:
        form = LoginForm()
        return render(request,
                      'registration/login.html',
                      {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})


def register(request):
    if request.method == 'POST':
        print("===========request object===========", request)
        print("request method", request.method)
        user_form = UserRegistrationForm(request.POST)
        print("user_form:-", user_form)
        if user_form.is_valid():
            print("Validation after user_form")
            # Create a new user object but avoid to save it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})

    else:
        user_form = UserRegistrationForm()
        return render(request,
                      'account/register.html',
                      {'user_form': user_form})