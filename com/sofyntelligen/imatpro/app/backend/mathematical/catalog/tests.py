from django.test import TestCase

# Python
import json

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status

# Models
from com.sofyntelligen.imatpro.app.models.system.equations.mathematical.models import TypeEquation, GradeSchool


class EducationTestCase(TestCase):
    def test_create_generic_catalog(self):

        client = APIClient()

        generic_catalog = {
            'data': [
                {
                    'value': 'qq',
                    'name': 'q',
                    'description': 'qq'
                },
                {
                    'value': 'q',
                    'name': 'qwwe',
                    'description': 'q'
                }
            ]
        }

        response = client.post(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all',
            generic_catalog,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('data', result)
        self.assertEqual(2, result['data'].__len__())

        if 'data' in result:
            del result['data'][0]['id']
            del result['data'][1]['id']

        self.assertEqual(result, result)

    def test_list_generic_catalog(self):

        client = APIClient()

        type_equation = TypeEquation.objects.create(
            value="test_text",
            name="test_text",
            description="test_text"
        )

        generic_catalog = {
            'data': [
                {
                    'value': 'qq',
                    'name': 'q',
                    'description': 'qq'
                },
                {
                    'value': 'q',
                    'name': 'qwwe',
                    'description': 'q'
                }
            ]
        }

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all?limit=100&offset=0',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

