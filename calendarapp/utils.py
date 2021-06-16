
# calendarapp/utils.py

from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event
from eventcalendar.helper import get_current_user

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		d += '<div class=""><a href="/add_event">+Add </a></div>'
	#add another field to show in calendar	
		for event in events_per_day:
			
			event_time = event.start_time.strftime("%d-%m-%Y %H:%M")
			# f_time = event_time.strftime("%d-%m-%Y %H:%M")
			if event.is_approved: 
				d += f'<li><button type="button" class="btn btn-primary btn-sm">{event.get_html_url} -{event_time}</button></li>'
				
			else: 
				d += f'<li><button type="button" class="btn btn-danger btn-sm">{event.get_html_url} Request Pending</button></li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal