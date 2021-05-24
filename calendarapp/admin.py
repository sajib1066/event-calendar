from django.contrib import admin
from calendarapp.models import Event, EventMember, Booking_Request, Room, Facility

class EventMemberAdmin(admin.ModelAdmin):
    model = EventMember
    list_display = ['event', 'user']

class Booking_Request_admin(admin.ModelAdmin):
    list_display = ['meeting_title']
    
class meta:
        model = Booking_Request


class Facility_admin(admin.ModelAdmin):
    model = Facility
    list_display = ['Facility']
    
class Room_admin(admin.ModelAdmin):
    model = Room
    list_display = ['Room']




admin.site.register(Event)
admin.site.register(EventMember, EventMemberAdmin)
admin.site.register(Booking_Request, Booking_Request_admin)
admin.site.register(Facility,Facility_admin)
admin.site.register(Room,Room_admin)

