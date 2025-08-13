import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone

from users import helpers


class DateTimeFormattingTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", password="pass"
        )

    def test_default_formatting(self):
        dt = datetime.datetime(2024, 1, 2, 3, 0, tzinfo=datetime.timezone.utc)
        formatted = helpers.format_datetime(dt, self.user)
        self.assertEqual(formatted, "2024-01-02 03:00")

    def test_custom_formats(self):
        self.user.date_format = "dmy"
        self.user.time_format = "12"
        self.user.save()
        dt = datetime.datetime(2024, 1, 2, 15, 0, tzinfo=datetime.timezone.utc)
        formatted = helpers.format_datetime(dt, self.user)
        self.assertEqual(formatted, "02/01/2024 3:00 PM")
