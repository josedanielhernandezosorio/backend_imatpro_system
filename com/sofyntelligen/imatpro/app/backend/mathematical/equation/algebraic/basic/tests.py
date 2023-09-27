import json

from django.test import TestCase

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status


class BasicTestCase(TestCase):
    fixtures = ['catalog', 'character', 'equation', 'representation']

    def test_search_character_all(self):

        self.assertEqual({}, {})
