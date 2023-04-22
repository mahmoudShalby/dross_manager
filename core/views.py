from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not all((username, password)):
      return JsonResponse({'exists': False})

    user = authenticate(request)
    if not user:
      return JsonResponse({'wrong': False})

    login(user)
    return redirect('/')

  return render(request, 'core/login.html', {})
