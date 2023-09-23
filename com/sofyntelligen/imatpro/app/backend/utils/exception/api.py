from rest_framework import status
from rest_framework.exceptions import APIException


class ImatProCustomException(APIException):
    detail = None
    code = None
    status_code = 499

    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'

    def __init__(self, detail, status_code, code):
        super().__init__(detail, status_code)
        self.detail = detail
        self.status_code = status_code
        self.code = code


class ImatProNotExistException(ImatProCustomException):

    def __init__(self, code, detail='No Content', status=status.HTTP_204_NO_CONTENT):
        super().__init__(detail, status, code)


class ImatProTokenNotValidException(ImatProCustomException):

    def __init__(self, code, detail='Invalid or absent JWT token field.', status=status.HTTP_403_FORBIDDEN):
        super().__init__(detail, status, code)


class ImatProNoAuthHeaderException(ImatProCustomException):

    def __init__(self, code, detail='Absent Authorization header.', status=status.HTTP_403_FORBIDDEN):
        super().__init__(detail, status, code)


class ImatProIntegrityException(ImatProCustomException):

    def __init__(self, code, detail='Conflict', status=status.HTTP_409_CONFLICT):
        super().__init__(detail, status, code)


class ImatProQueryParameterException(ImatProCustomException):

    def __init__(self, code, detail='Unsupported Media Type', status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE):
        super().__init__(detail, status, code)
