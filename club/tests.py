from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
from .forms import MeetingForm
from .forms import ResourceForm
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='Python Initial Meeting')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Python Initial Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class ResourceTest(TestCase):
    def setUp(self):
        self.type=Resource(resourcename='Codeacademy')
        self.user=User(username='user1')
        self.resource=Resource(resourcename='Codeacademy', resourcetype='Educational Platform', url='https://www.codeacademy.com/catalog/language/python', dateentered=('2021-05-14'), userid=self.user, description='An educational platform with free coding classes')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Codeacademy')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class newMeetingForm(TestCase):
    #valid form data
    def test_meetingForm(self):
        data={
            'meetingtitle': 'Another Python Meeting',
             'meetingdate': '2021-07-01',
             'meetingtime': '10:30 PM',
             'location': 'Virtual (Zoom)',
             'agenda': 'Follow up',
        }
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)

class newResourceForm(TestCase):
    #valid form data
    def test_ResourceForm(self):
        data={
            'resourcename': 'Udemy',
             'resourcetype': 'Online course',
             'url': 'https://www.udemy.com/topic/python/',
             'dateentered': '2021-06-03',
             'userid': 'intisar',
             'description': 'An online course provider with a specialty for programming',
        }
        form=ResourceForm (data)
        self.assertTrue(form.is_valid)

class New_Resource_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@$$w0rd1')
        self.type=Resource.objects.create(resourcename='Codeacademy')
        self.resource=Resource.objects.create(resourcename='Codeacademy', resourcetype='Educational Platform', url='https://www.codeacademy.com/catalog/language/python', dateentered=('2021-05-14'), userid=self.test_user, description='An educational platform with free coding classes')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newresource/')