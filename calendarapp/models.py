from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import timedelta

class Facility(models.Model):
    Facility = models.CharField(max_length=200)
    def __str__(self):
        return self.Facility
    def __unicode__(self):
        return self.Facility



class Room(models.Model):
    Room = models.CharField(max_length=200)
    #Facility = models.ManyToManyField(Facility)
    def __str__(self):
        return self.Room
    def __unicode__(self):
        return self.Room

class Event(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    #title = models.CharField(max_length=200, unique=True) was orginal data field
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    phone = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('calendarapp:event-detail', args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse('calendarapp:event-detail', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


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
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    #number_of_person = models.IntegerField(blank=True, null=True)
    isComplete = models.BooleanField(default=False)
    def __str__(self):
        return self.meeting_title 
    def __unicode__(self):
        return self.meeting_title
    
