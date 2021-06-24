from django.views.generic import View
from django.shortcuts import render


class SignInView(View):
    """ User registration view """
    template_name = 'accounts/signin.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
