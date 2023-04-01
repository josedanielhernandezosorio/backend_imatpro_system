from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict


class CustomNumberPagination(pagination.PageNumberPagination):

    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 200
    page_query_param = 'page'

    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'pagination': {
                'count': self.page.paginator.count,
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                    }
                }
            }
        )


class CustomLimitOffsetPagination(pagination.LimitOffsetPagination):

    default_limit = 20
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 200

    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'pagination': {
                'count': self.page.paginator.count,
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                    }
                }
            }
        )