from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getFirstDegree(request):
    firstdegree = [
        "Hello, world",
        "You're at the polls index."
    ]
    return Response(firstdegree)
