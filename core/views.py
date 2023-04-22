from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    if all((username, password)):
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('/')

      messages.add_message(request, messages.error, 'Wrong username or password')

  return render(request, 'core/login.html')
