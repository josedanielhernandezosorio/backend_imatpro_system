import logging
import logging.config

from rest_framework import pagination
from rest_framework.response import Response
from rest_framework import status


class CustomNumberPagination(pagination.PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 200

    def get_paginated_response(self, data):
        return get_response(self, data, True)


class CustomLimitOffsetPagination(pagination.LimitOffsetPagination):
    max_limit = 200

    def get_paginated_response(self, data):
        return get_response(self, data, False)


def get_response(self, data, type_pagination):
    if 0 < len(data):
        return Response({
            'data': data,
            'pagination': {
                'count': self.page.paginator.count if type_pagination else self.count,
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                }
            }
        }, status=status.HTTP_200_OK)
    else:
        return Response({}, status=status.HTTP_204_NO_CONTENT)
