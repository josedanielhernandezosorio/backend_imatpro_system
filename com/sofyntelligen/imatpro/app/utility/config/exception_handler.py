import logging
import logging.config

from rest_framework.views import exception_handler
from rest_framework import status

from datetime import datetime


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:

        if response.status_code == status.HTTP_401_UNAUTHORIZED:
            logging.getLogger('error_logger').error(response.data)
            return response

        if response.status_code == status.HTTP_204_NO_CONTENT:
            response.data = {}
            return response

        if response.status_code != status.HTTP_204_NO_CONTENT:
            response.data['message'] = response.data['detail']
            response.data['code'] = exc.code
            response.data['date'] = datetime.now()
            del response.data['detail']
            logging.getLogger('error_logger').error(response.data)
            return response

    return response
