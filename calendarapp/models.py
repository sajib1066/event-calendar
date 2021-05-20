from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('calendarapp:event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('calendarapp:event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} {self.date} {self.start_time} </a>'


class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.user)



class Booking_Request(models.Model):
    
    meeting_title = models.CharField(max_length=200)
    description = models.TextField()
    Date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=200)
    
    isComplete = models.BooleanField(default=False)
    def __str__(self):
        return self.meeting_title 
    def __unicode__(self):
        return self.meeting_title
    