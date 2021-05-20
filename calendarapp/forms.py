from django.forms import ModelForm, DateInput
from calendarapp.models import Event, EventMember, Booking_Request
from django import forms

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
     
    }
    exclude = ['user']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    #self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    #self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)



class SignupForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class AddMemberForm(forms.ModelForm):
  class Meta:
    model = EventMember
    fields = ['user']

class Booking_RequestForm(forms.ModelForm):
  class Meta:
    model = Booking_Request
    fields = '__all__'
