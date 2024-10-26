from datetime import datetime
from django.db import models
from django.urls import reverse

from calendarapp.models import EventAbstract
from accounts.models import User
from sport.models.sport import NULLABLE


class EventManager(models.Manager):
    """ Event manager """

    def get_all_events(self, user):
        events = Event.objects.filter(user=user, is_active=True, is_deleted=False)
        return events

    def get_running_events(self, user):
        running_events = Event.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            end_time__gte=datetime.now(),
            start_time__lte=datetime.now()
        ).order_by("start_time")
        return running_events

    def get_completed_events(self, user):
        completed_events = Event.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            end_time__lt=datetime.now(),
        )
        return completed_events

    def get_upcoming_events(self, user):
        upcoming_events = Event.objects.filter(
            user=user,
            is_active=True,
            is_deleted=False,
            start_time__gt=datetime.now(),
        )
        return upcoming_events


class Event(EventAbstract):
    """ Event model """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    trainer = models.ForeignKey(
        "sport.Trainer", on_delete=models.SET_NULL, related_name="events", null=True
    )
    title = models.CharField(max_length=200)
    description = models.TextField(**NULLABLE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    direction = models.ForeignKey(
        "sport.Direction", on_delete=models.SET_NULL, related_name="events", null=True
    )
    max_participants = models.PositiveIntegerField(default=0, **NULLABLE)

    objects = EventManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("calendarapp:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("calendarapp:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"
