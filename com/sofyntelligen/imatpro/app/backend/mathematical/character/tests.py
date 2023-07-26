import json

from django.test import TestCase

# Django Rest Framework
from rest_framework.test import APIClient
from rest_framework import status


class CharacterTestCase(TestCase):
    fixtures = ['character']

    def test_create_character_all(self):

        client = APIClient()

        character_exception = {
            'data': [
                {
                    'view_text': '1',
                    'view_latex': '1',
                    'view': '1',
                    'description': 'NUMERO UNO'
                }
            ]
        }

        characters = {
            'data': [
                {
                    'view_text': '11',
                    'view_latex': '11',
                    'view': '11',
                    'description': 'NUMERO UNO'
                },
                {
                    'view_text': '21',
                    'view_latex': '21',
                    'view': '21',
                    'description': 'NUMERO DOS'
                },
                {
                    'view_text': '31',
                    'view_latex': '31',
                    'view': '31',
                    'description': 'NUMERO TRES'
                }
            ]
        }

        response = client.post(
            '/imatpro/api/v1.0.0/mathematical/character/all',
            characters,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertIn('data', result)
        self.assertEqual(3, result['data'].__len__())

        if 'data' in result:
            del result['data'][0]['id']
            del result['data'][1]['id']
            del result['data'][2]['id']
            del result['data'][0]['date']
            del result['data'][1]['date']
            del result['data'][2]['date']
            del result['data'][0]['last_update']
            del result['data'][1]['last_update']
            del result['data'][2]['last_update']

        self.assertEqual(characters, result)

        response = client.post(
            '/imatpro/api/v1.0.0/mathematical/character/all',
            character_exception,
            format='json'
        )

        # TODO: error code definition
        result = json.loads(response.content)
        self.assertEqual(status.HTTP_409_CONFLICT, response.status_code)
        self.assertIn('message', result)
        self.assertIn('code', result)
        self.assertIn('date', result)

    def test_search_character_all(self):

        client = APIClient()

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/character/all',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(20, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/character/all?limit=100&offset=0',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(100, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/character/all?limit=100&offset=188',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/character/all?limit=1&offset=188',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/character/all?offset=0',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(20, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/character/all?offset=180',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(8, result['data'].__len__())

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/character/all?offset=188',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/character/all?limit=1',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('data', result)
        self.assertIn('pagination', result)
        self.assertEqual(1, result['data'].__len__())

    def test_create_character(self):

        client = APIClient()

        character_exception = {
            'view_text': '1',
            'view_latex': '1',
            'view': '1',
            'description': 'NUMERO UNO'
        }

        character = {
            'view_text': '111',
            'view_latex': '111',
            'view': '111',
            'description': 'NUMERO UNO'
        }

        response = client.post(
            '/imatpro/api/v1.0.0/mathematical/character/',
            character,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertIn('id', result)
        self.assertIn('view_text', result)
        self.assertIn('view_latex', result)
        self.assertIn('view', result)
        self.assertIn('description', result)
        self.assertIn('date', result)

        if result != None:
            del result['id']
            del result['date']
            del result['last_update']

        self.assertEqual(character, result)

        response = client.post(
            '/imatpro/api/v1.0.0/mathematical/character/',
            character_exception,
            format='json'
        )

        # TODO: error code definition
        result = json.loads(response.content)
        self.assertEqual(status.HTTP_409_CONFLICT, response.status_code)
        self.assertIn('message', result)
        self.assertIn('code', result)
        self.assertIn('date', result)

    def test_update_character(self):

        client = APIClient()

        character = {
            'view_text': '111',
            'view_latex': '111',
            'view': '111',
            'description': 'NUMERO UNO'
        }

        response = client.put(
            '/imatpro/api/v1.0.0/mathematical/character/111',
            character,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('id', result)
        self.assertIn('view_text', result)
        self.assertIn('view_latex', result)
        self.assertIn('view', result)
        self.assertIn('description', result)
        self.assertIn('date', result)

        if result != None:
            del result['id']
            del result['date']
            del result['last_update']

        self.assertEqual(character, result)

        response = client.put(
            '/imatpro/api/v1.0.0/mathematical/character/1000',
            character,
            format='json'
        )

        # TODO: error code definition
        result = json.loads(response.content)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertIn('message', result)
        self.assertIn('code', result)
        self.assertIn('date', result)

    def test_delete_character(self):
        client = APIClient()

        response = client.delete(
            '/imatpro/api/v1.0.0/mathematical/character/1',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.delete(
            '/imatpro/api/v1.0.0/mathematical/character/1',
            format='json'
        )

        # TODO: error code definition
        result = json.loads(response.content)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        self.assertIn('message', result)
        self.assertIn('code', result)
        self.assertIn('date', result)

    def test_get_character(self):

        client = APIClient()

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/character/1000',
            format='json'
        )

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual({}, response.data)

        response = client.get(
            '/imatpro/api/v1.0.0/mathematical/character/170',
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertIn('id', result)
        self.assertIn('view_text', result)
        self.assertIn('view_latex', result)
        self.assertIn('view', result)
        self.assertIn('description', result)
        self.assertIn('date', result)
