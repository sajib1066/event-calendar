# cal/views.py

from datetime import datetime, date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta
import calendar
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
#extra page use for practice
from calendarapp.models import Booking_Request

from .models import *
from .utils import Calendar
from .forms import AddMemberForm, Booking_RequestForm, Event_Form


@login_required(login_url='signup')
def index(request):
    return HttpResponse('hello')

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
#need delete login requiredminin and login url to show calendar to all
class CalendarView(generic.ListView):
    
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context
#need delete login requiredminin and login url to show calendar to all
class CalendarView1(LoginRequiredMixin, generic.ListView):
    login_url = 'signup'
    model = Event
    template_name = 'calendar_admin.html'
#
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

@login_required(login_url='signup')
def create_event_1(request):
    form = EventForm(request.POST or None)
    all_Rooms = Room.objects.all()
    if request.POST and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        Event.objects.get_or_create(
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
            Room = form.cleaned_data['Room'],
        )
    
    return render(request, 'calendar.html', locals())

#@login_required(login_url='signup')
@login_required(login_url='signup')
def create_event(request):    
    form = EventForm(request.POST or None)
    all_Rooms = Room.objects.all()
    if request.POST and form.is_valid():
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']
        Event.objects.get_or_create(
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
            Room = form.cleaned_data['Room'],
        )
        # return render(request, reverse('calendarapp:calendar'), locals())
        return HttpResponseRedirect(reverse('calendarapp:calendar'))
    return render(request, 'event.html', {'form': form})





class EventEdit(generic.UpdateView):
    model = Event
    fields = ['user','title', 'description', 'start_time', 'end_time','Room','phone','email', 'is_approved']
    template_name = 'event.html'

def RoomEdit(request, room_id):
    get_room = get_object_or_404(Room, pk=room_id)
    room_detail = Room.objects.all()
    template_name = 'room.html'

    form = request.POST
    if form:
        get_room.Room = form.get('Room')
        get_room.save()
        verified = True

    return render(request, template_name, locals())




@login_required(login_url='signup')
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    eventmember = EventMember.objects.filter(event=event)
    context = {
        'event': event,
        'eventmember': eventmember
    }
    return render(request, 'event-details.html', context)


def add_eventmember(request, event_id):
    forms = AddMemberForm()
    if request.method == 'POST':
        forms = AddMemberForm(request.POST)
        if forms.is_valid():
            member = EventMember.objects.filter(event=event_id)
            event = Event.objects.get(id=event_id)
            if member.count() <= 9:
                user = forms.cleaned_data['user']
                EventMember.objects.create(
                    event=event,
                    user=user
                )
                return redirect('calendarapp:calendar')
            else:
                print('--------------User limit exceed!-----------------')
    context = {
        'form': forms
    }
    return render(request, 'add_member.html', context)

class EventMemberDeleteView(generic.DeleteView):
    model = EventMember
    template_name = 'event_delete.html'
    success_url = reverse_lazy('calendarapp:calendar')


def book_room_form(request):
    form = Booking_RequestForm(request.POST)
    # form = request.POST

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        verified = True
        print(verified)
    else:
        print('not verified')
    return render(request, 'book_room.html', locals())

#testinf form for expirement
def sample_form(request):
    form = Booking_RequestForm(request.POST)
    # form = request.POST

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        verified = True
        print(verified)
    else:
        print('not verified')
    return render(request, 'sample.html', locals())

#testing1 form for expirement
def Add_Event(request):
    form = Event_Form(request.POST)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        verified = True
        print(verified)
        return redirect('/') 
    else:
        print('not verified')
    return render(request, 'add_event.html', locals())
    
def Edit_Event(request, id):
    form = Event_Form(request.POST)
    data = get_object_or_404(Event, pk=id)
    
    # records = Event.objects.all()
    # record2 = Event.objects.filter(title='first').order_by('start_time')
    # form = request.POST
    data.Room = 'new room'
    # data.
    form.Room = data.Room
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        verified = True
        print(verified)
        return redirect('/') 
    else:
        print('not verified')
    return render(request, 'add_event.html', locals())


# Create to practice show data in taBLE Query
def all_request(request):
    allrequest = Booking_Request.objects.all()
    return render(request,'All_request.html',{'allreq':allrequest})
# Show all created booking request by the end user
def pending_request(request):
    pendingrequest = Event.objects.all()

    if request.POST:
        form = request.POST
        booking_id = form["booking_id"]
        booking_to_edit = get_object_or_404(Event, id=booking_id)
        booking_to_edit.is_approved = True
        #booking_to_edit.description = "32"
        booking_to_edit.save()

    return render(request,'Pending_request.html',{'pendingreq':pendingrequest})

# Show all approved by the District Manger/admin 
def approved_request(request):
    approvedrequest = Event.objects.all()
    return render(request,'Approved_request.html',{'approvedreq':approvedrequest})
    

# Show all approved by the District Manger/admin 
def view_rooms(request):
    room_detail = Room.objects.all()
    return render(request,'room_details.html',{'room_det':room_detail})


