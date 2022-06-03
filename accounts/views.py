from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from . import forms


class LoginView(View):
    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
        else:
            return render(request, 'login.html', {'error': 'Invalid data for the form',
                                                  'form': forms.LoginForm()})

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        return render(request, 'login.html', {'error': 'User not found',
                                              'form': forms.LoginForm()})

    def get(self, request):
        return render(request, 'login.html', {'form': forms.LoginForm()})


@login_required
def mock(request):
    return HttpResponse('Successfully logged in')


def logout_view(request):
    logout(request)
    return HttpResponse('Successfully logged out')
