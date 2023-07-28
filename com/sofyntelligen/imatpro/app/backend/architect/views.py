from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getFirstDegree(request):
    firstdegree = [
        'ARCHITECT READY',
        'valid test junit and valid status componentes'
    ]
    return Response(firstdegree)
