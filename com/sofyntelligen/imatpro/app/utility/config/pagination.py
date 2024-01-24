import logging
import logging.config

from rest_framework import pagination
from rest_framework.response import Response
from rest_framework import status


class CustomNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return get_response(self, data)


def get_response(self, data):
    if 0 < len(data):
        return Response({
            'data': data,
            'pagination': {
                'pages': self.page.paginator.num_pages,
                'count': self.page.paginator.count,
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                }
            }
        }, status=status.HTTP_200_OK)
    else:
        return Response({}, status=status.HTTP_204_NO_CONTENT)
