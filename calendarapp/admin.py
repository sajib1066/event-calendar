from django.contrib import admin
from calendarapp.models import Event, EventMember,Booking_Request

class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ['event', 'user']

class Booking_Request_admin(admin.ModelAdmin):
    list_display = ['meeting_title']
    
class meta:
        model = Booking_Request


admin.site.register(Event)
admin.site.register(EventMember, EventMemberAdmin)
admin.site.register(Booking_Request, Booking_Request_admin)
