import json

from django.test import TestCase

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status


class EquationTestCase(TestCase):
    fixtures = ['catalog', 'character', 'equation', 'representation']

    def test_search_character_all(self):
        client = APIClient()

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/all',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(2, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/all?limit=100&offset=1&type_representation=ALL',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(8, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/all?limit=1&offset=1',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(1, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/all?type_equations=EPR01',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(2, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/all?grade_school=PRI01',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(2, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/all?type_representation=PRINCIPAL',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(2, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/all?limit=100&offset=100',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)
