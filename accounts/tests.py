from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth import logout

from accounts.forms import SignInForm

User = get_user_model()  # Get the user model


class SignInViewTests(TestCase):
    """ Tests for the SignInView """

    def setUp(self):
        # URL for the signin page
        self.signin_url = reverse('accounts:signin')
        # Create a test user
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='password123'
        )

    def test_signin_get(self):
        """ Test that the signin page loads correctly """
        response = self.client.get(self.signin_url)
        
        # Check that the response is 200 OK
        self.assertEqual(response.status_code, 200)
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'accounts/signin.html')
        # Check that the form is present in the context
        self.assertIsInstance(response.context['form'], SignInForm)

    def test_signin_post_valid_data(self):
        """ Test signin with valid credentials """
        valid_data = {
            'email': 'testuser@example.com',
            'password': 'password123'
        }
        response = self.client.post(self.signin_url, data=valid_data)
        
        # Check that a redirect occurs after successful login
        self.assertRedirects(response, reverse('calendarapp:calendar'))
        # Check that the user is logged in
        self.assertEqual(response.wsgi_request.user, self.user)

    def test_signin_post_invalid_data(self):
        """ Test signin with invalid credentials """
        invalid_data = {
            'email': 'wronguser@example.com',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.signin_url, data=invalid_data)
        
        # Check that the response is still 200 OK
        self.assertEqual(response.status_code, 200)
        # Check that the form is still in the context (indicating the page is rendered again)
        self.assertIsInstance(response.context['form'], SignInForm)
        # Check that the user is not logged in
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_signin_post_missing_fields(self):
        """ Test signin with missing fields """
        response = self.client.post(self.signin_url, data={})
        
        # Check that the response is still 200 OK
        self.assertEqual(response.status_code, 200)
        # Check that the form is still in the context
        self.assertIsInstance(response.context['form'], SignInForm)
        # Check that no user is logged in
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class SignOutViewTests(TestCase):
    """ Tests for the signout view """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='password123'
        )
        self.signout_url = reverse('accounts:signout')  # URL for the signout view

    def test_signout_redirect(self):
        """ Test that the user is logged out and redirected correctly """
        # Log in the user
        self.client.login(email='testuser@example.com', password='password123')
        
        # Check that the user is logged in
        response = self.client.get(reverse('accounts:signin'))  # You can replace this with any view that requires authentication
        self.assertEqual(response.status_code, 200)

        # Call the signout view
        response = self.client.get(self.signout_url)
        
        # Check that the user is redirected to the signing page
        self.assertRedirects(response, reverse('accounts:signin'))

        # Check that the user is logged out
        # Attempt to access a page that requires authentication
        response = self.client.get(reverse('accounts:signin'))
        self.assertEqual(response.status_code, 200)  # User should still be able to access the sign-in page
        self.assertFalse(response.wsgi_request.user.is_authenticated)  # Ensure the user is logged out


class SignOutViewTests(TestCase):
    """ Tests for the signout view """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            email='testuser@example.com',  # Change this to email if using email as username
            password='password123'
        )
        self.signout_url = reverse('accounts:signout')  # URL for the signout view
        self.signing_url = reverse('accounts:signin')  # URL to redirect to after signing out

    def test_signout_redirect(self):
        """ Test that the user is logged out and redirected correctly """
        # Log in the user
        self.client.login(email='testuser@example.com', password='password123')
        
        # Ensure the user is logged in
        self.assertTrue(self.client.session['_auth_user_id'])
        
        # Call the signout view
        response = self.client.get(self.signout_url)
        
        # Check that the user is redirected to the signing page
        self.assertRedirects(response, self.signing_url)

        # Check that the user is logged out
        self.assertFalse('_auth_user_id' in self.client.session)  # Ensure user ID is removed from session
        self.assertFalse(response.wsgi_request.user.is_authenticated)  # Ensure the user is logged out

    def test_signout_anonymous_user(self):
        """ Test that an anonymous user can access the signout view and is redirected """
        # Call the signout view without logging in
        response = self.client.get(self.signout_url)

        # Check that the user is redirected to the signing page
        self.assertRedirects(response, self.signing_url)
