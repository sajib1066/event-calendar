from django.http import JsonResponse
from django.views.generic import ListView

from calendarapp.models import Event


class EventsListView(ListView):
    template_name = "calendarapp/events_list.html"
    model = Event

    def render_to_response(self, context, **response_kwargs):
        # Проверяем, что запрос требует JSON
        if self.request.headers.get('Accept') == 'application/json':
            events = list(self.get_queryset().values())  # Преобразуем QuerySet в список словарей
            return JsonResponse(events, safe=False)  # Возвращаем JSON ответ
        else:
            # Если не JSON, рендерим стандартный HTML-шаблон
            return super().render_to_response(context, **response_kwargs)


class AllEventsListView(EventsListView):
    """ All event list views """

    def get_queryset(self):
        return Event.objects.get_all_events(user=self.request.user)


class RunningEventsListView(EventsListView):
    """ Running events list view """

    def get_queryset(self):
        return Event.objects.get_running_events(user=self.request.user)


class UpcomingEventsListView(EventsListView):
    """ Upcoming events list view """

    def get_queryset(self):
        return Event.objects.get_upcoming_events(user=self.request.user)


class CompletedEventsListView(EventsListView):
    """ Completed events list view """

    def get_queryset(self):
        return Event.objects.get_completed_events(user=self.request.user)
