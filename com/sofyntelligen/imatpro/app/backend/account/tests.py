import json

from django.test import TestCase

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status


class EducationTestCase(TestCase):
    fixtures = ['catalog']

    def test_create_generic_catalog_all(self):

        client = APIClient()

        generic_catalog_exception = {
            'data': [
                {
                    'value': 'EPR01',
                    'name': '',
                    'description': ''
                 }
            ]
        }

        generic_catalog = {
            'data': [
                {
                    'value': 'test1',
                    'name': 'test_text1',
                    'description': 'test_text1'
                },
                {
                    'value': 'test2',
                    'name': 'test_text2',
                    'description': 'test_text2'
                }
            ]
        }

        response = client.post(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all',
            generic_catalog,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertIn('data', result)
        self.assertEqual(2, result['data'].__len__())

        if 'data' in result:
            del result['data'][0]['id']
            del result['data'][1]['id']

        self.assertEqual(generic_catalog, result)

        response = client.post(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all',
            generic_catalog,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertIn('data', result)
        self.assertEqual(2, result['data'].__len__())

        if 'data' in result:
            del result['data'][0]['id']
            del result['data'][1]['id']

        self.assertEqual(generic_catalog, result)

        response = client.post(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all',
            generic_catalog_exception,
            format='json'
        )

        # TODO: add more functionality for html 400 status handling
        result = json.loads(response.content)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_search_generic_catalog_all(self):

        client = APIClient()

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(3, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all?limit=100&offset=0',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(3, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all?limit=100&offset=10',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all?limit=1&offset=10',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all?offset=0',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(3, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all?offset=1',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(2, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all?offset=10',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all?limit=1',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(1, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(20, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all?limit=100&offset=0',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(24, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all?limit=100&offset=25',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all?limit=1&offset=25',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all?offset=0',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(20, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all?offset=3',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(20, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all?offset=25',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all?limit=1',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(1, result['data'].__len__())

