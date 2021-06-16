from django.urls import path

from . import views
from calendarapp import views as CalendarViewapp


app_name = 'calendarapp'
urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.create_event, name='event_new'),
    path('event/edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'),
    path('event/<int:event_id>/details/', views.event_details, name='event-detail'),
    path('add_eventmember/<int:event_id>', views.add_eventmember, name='add_eventmember'),
    path('event/<int:pk>/remove', views.EventMemberDeleteView.as_view(), name="remove_event"),
    path('book_room_urlpath',CalendarViewapp.book_room_form),
    path('add_event',CalendarViewapp.Add_Event),
    path('pending_request_url',CalendarViewapp.pending_request),
    path('approved_request_url',CalendarViewapp.approved_request),
    path('All_request_url',CalendarViewapp.all_request),
    path('app_admin',views.CalendarView1.as_view(), name='calendar'),
    path('room/edit/<int:room_id>/', CalendarViewapp.RoomEdit),
    path('room/edit/save/<int:room_id>/', CalendarViewapp.RoomEdit),
    path('viewrooms',CalendarViewapp.view_rooms),
]