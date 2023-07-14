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

        TypeEquation.objects.create(value="test", name="test_text", description="test_text")
        GradeSchool.objects.create(value="test", name="test_text", description="test_text")

        generic_catalog_exception = {
            'data': [
                {
                    'id': 1,
                    'value': 'test_text',
                    'name': 'test_text',
                    'description': 'test_text'
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

    def test_list_generic_catalog(self):

        client = APIClient()

        TypeEquation.objects.create(value="test", name="test_text", description="test_text")
        TypeEquation.objects.create(value="test1", name="test_text2", description="test_text")
        TypeEquation.objects.create(value="test2", name="test_text3", description="test_text")
        TypeEquation.objects.create(value="test3", name="test_text4", description="test_text")
        TypeEquation.objects.create(value="test4", name="test_text5", description="test_text")

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(5, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all?limit=100&offset=0',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(5, result['data'].__len__())

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
        self.assertEqual(5, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/type_equation/all?offset=3',
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

        GradeSchool.objects.create(value="test", name="test_text", description="test_text")
        GradeSchool.objects.create(value="test1", name="test_text2", description="test_text")
        GradeSchool.objects.create(value="test2", name="test_text3", description="test_text")
        GradeSchool.objects.create(value="test3", name="test_text4", description="test_text")
        GradeSchool.objects.create(value="test4", name="test_text5", description="test_text")

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(5, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all?limit=100&offset=0',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(5, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all?limit=100&offset=10',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all?limit=1&offset=10',
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
        self.assertEqual(5, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all?offset=3',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(2, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/catalog/grade_school/all?offset=10',
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

