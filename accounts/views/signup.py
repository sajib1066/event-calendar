from django.views.generic import View
from django.shortcuts import render


class SignUpView(View):
    """ User registration view """
    template_name = 'accounts/signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
