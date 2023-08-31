from django.shortcuts import render

import os
import sys
from os import system, remove
from uuid import uuid4

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_state_architect(request):

    state = 'ARCHITECT_NOT_READY'

    if os.path.exists("manage.py") and \
            os.system("source virtual-backend-imatpro-system/bin/activate") == 0 and \
            os.system("python manage.py test --settings=settings.test") == 0:
        state = 'ARCHITECT_READY : valid test and components in OK state'

    return Response([state])


