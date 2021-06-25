from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from calendarapp.models import Event


class DashboardView(LoginRequiredMixin, View):
    login_url = 'accounts:signin'
    template_name = 'calendarapp/dashboard.html'

    def get(self, request, *args, **kwargs):
        events = Event.objects.filter(
            user=request.user, is_active=True, is_deleted=False
        )
        context = {
            'total_event': events.count()
        }
        return render(request, self.template_name, context)
