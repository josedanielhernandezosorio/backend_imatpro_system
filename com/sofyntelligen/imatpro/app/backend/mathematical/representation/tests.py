import json

from django.test import TestCase

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status


class RepresentationTestCase(TestCase):
    fixtures = ['catalog', 'character', 'equation', 'representation']

    def test_search_character_all(self):
        client = APIClient()

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/representation/all',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(9, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/representation/all?solution_id=a837109a-aacb-44db-b64d-f8278c9643c1',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(6, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/representation/all?limit=2&offset=3&solution_id=a837109a-aacb-44db-b64d-f8278c9643c1',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(2, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/representation/all?solution_id=a837109a-aacb-55bd-b64d-f8278c9643c1',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/representation/all?offset=3&solution_id=a837109a-aacb-44db-b64d-f8278c9643c1',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(3, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/representation/all?limit=2&solution_id=a837109a-aacb-44db-b64d-f8278c9643c1',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(2, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/equation/representation/all?limit=100&offset=10&solution_id=a837109a-aacb-44db-b64d-f8278c9643c1',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)
