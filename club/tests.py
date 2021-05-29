from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Resource, Event
import datetime
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

    