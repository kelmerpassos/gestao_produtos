from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def sing_out(request):
    logout(request)
    return redirect('login')


@login_required
def get_index(request):
    return render(request, 'index.html')
