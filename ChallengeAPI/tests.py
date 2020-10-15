from django.test import TestCase
from .models import Challenge
from .views import ChallengeView,ChallengeDetail
# Create your tests here.

class ChallengeModelTestCase(TestCase):

    def test_evaluate_array(self):
        self.assertEqual(Challenge.evaluate_array(items=[1,2,[3,4,[5,6],7],8]),{"result":[1,2,3,4,5,6,7,8]})


class ChallengeViewTestCase(TestCase):
    
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('http://localhost:8000/api/challenge')
        self.assertEqual(response.status_code, 301)

