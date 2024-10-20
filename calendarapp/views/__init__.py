from .event_list import AllEventsListView, CompletedEventsListView, RunningEventsListView, UpcomingEventsListView
from .other_views import (
    CalendarViewNew,
    CalendarView,
    create_event,
    EventEdit,
    event_details,
    add_eventmember,
    EventMemberDeleteView,
    delete_event,
    next_week,
    next_day,
)


__all__ = [
    AllEventsListView,
    RunningEventsListView,
    UpcomingEventsListView,
    CompletedEventsListView,
    CalendarViewNew,
    CalendarView,
    create_event,
    EventEdit,
    event_details,
    add_eventmember,
    EventMemberDeleteView,
    delete_event,
    next_week,
    next_day,
]
