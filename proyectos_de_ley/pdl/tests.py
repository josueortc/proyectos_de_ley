from django.test import TestCase
from pdl.management.commands.scraper import Command

# Create your tests here.
class ScrapperTest(TestCase):
    def test_url(self):
        x = Command()
        self.assertEqual("a", x.handle())
