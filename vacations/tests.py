from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Vacation
from datetime import date

class VacationModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Assuming your user model uses email instead of username for identification
        cls.user = get_user_model().objects.create_user(
            email='test@example.com', password='testpass123'
        )

    def test_vacation_creation(self):
        vacation = Vacation.objects.create(
            user=self.user,
            start_date=date(2023, 1, 1),
            end_date=date(2023, 1, 10)
        )

        self.assertTrue(isinstance(vacation, Vacation))
        self.assertEqual(vacation.user, self.user)
        self.assertEqual(vacation.start_date, date(2023, 1, 1))
        self.assertEqual(vacation.end_date, date(2023, 1, 10))
