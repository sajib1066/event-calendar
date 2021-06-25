from django.db import models

from django.contrib.auth.models import User

from calendarapp.models import Event, EventAbstract


class EventMember(EventAbstract):
    """ Event member model """
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.user)
