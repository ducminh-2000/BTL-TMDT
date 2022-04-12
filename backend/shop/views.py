import statistics
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from shop.models import *

@api_view(['GET'])
def detail(request):
    # find Author by pk (id)
    try: 
        author = Dress.objects.all()
        return Response({"data": author})
    except Dress.DoesNotExist: 
        return JsonResponse({'message': 'The Author does not exist'}, status=statistics.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE Author


