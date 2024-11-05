

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from calendarapp.models import Event

User = get_user_model()  # Get the user model

class EventListViewTests(TestCase):
    """ Tests for the Event list views """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            email='testuser@example.com', 
            password='password123'
        )
        self.client.login(email='testuser@example.com', password='password123')
        
        # Create some test events
        self.all_events_url = reverse('calendarapp:all_events')  # URL for AllEventsListView
        self.running_events_url = reverse('calendarapp:running_events')  # URL for RunningEventsListView
        self.upcoming_events_url = reverse('calendarapp:upcoming_events')  # URL for UpcomingEventsListView
        self.completed_events_url = reverse('calendarapp:completed_events')  # URL for CompletedEventsListView

        # Creating events for testing
        self.event1 = Event.objects.create(title="Past Event", user=self.user, start_time="2023-10-01", end_time="2023-10-01")  # Completed event
        self.event2 = Event.objects.create(title="Running Event", user=self.user, start_time="2024-11-01", end_time="2024-11-01")  # Running event
        self.event3 = Event.objects.create(title="Upcoming Event", user=self.user, start_time="2024-12-01", end_time="2024-12-01")  # Upcoming event
        self.event4 = Event.objects.create(title="Another Completed Event", user=self.user, start_time="2023-09-01", end_time="2023-09-01")  # Completed event

    def test_all_events_view(self):
        """ Test that all events are listed correctly """
        response = self.client.get(self.all_events_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calendarapp/events_list.html')
        self.assertIn(self.event1, response.context['object_list'])
        self.assertIn(self.event2, response.context['object_list'])
        self.assertIn(self.event3, response.context['object_list'])
        self.assertIn(self.event4, response.context['object_list'])

    def test_running_events_view(self):
        """ Test that only running events are listed """
        response = self.client.get(self.running_events_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calendarapp/events_list.html')
        self.assertNotIn(self.event2, response.context['object_list'])  # Running event should be in the list
        self.assertNotIn(self.event1, response.context['object_list'])  # Completed event should not be in the list
        self.assertNotIn(self.event3, response.context['object_list'])  # Upcoming event should not be in the list
        self.assertNotIn(self.event4, response.context['object_list'])  # Another completed event should not be in the list

    def test_upcoming_events_view(self):
        """ Test that only upcoming events are listed """
        response = self.client.get(self.upcoming_events_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calendarapp/events_list.html')
        self.assertIn(self.event3, response.context['object_list'])  # Upcoming event should be in the list
        self.assertNotIn(self.event1, response.context['object_list'])  # Completed event should not be in the list
        self.assertNotIn(self.event2, response.context['object_list'])  # Running event should not be in the list
        self.assertNotIn(self.event4, response.context['object_list'])  # Another completed event should not be in the list

    def test_completed_events_view(self):
        """ Test that only completed events are listed """
        response = self.client.get(self.completed_events_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'calendarapp/events_list.html')
        self.assertIn(self.event1, response.context['object_list'])  # Completed event should be in the list
        self.assertIn(self.event4, response.context['object_list'])  # Another completed event should also be in the list
        self.assertIn(self.event2, response.context['object_list'])  # Running event should not be in the list
        self.assertNotIn(self.event3, response.context['object_list'])  # Upcoming event should not be in the list
