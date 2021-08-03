from django.shortcuts import redirect
from django.contrib.auth import logout


def signout(request):
    logout(request)
    return redirect("accounts:signin")
