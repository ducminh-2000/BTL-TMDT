from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers



from shop.serializers import *
class AuthorDAO:
    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            author = list(Author.objects.values())
            return JsonResponse(author, safe=False)
        except Author.DoesNotExist: 
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    @api_view(['GET'])
    def getById(request,id):
        try:
            author = Author.objects.get(id=id)
            return JsonResponse((AuthorSer(author).data), safe=False)
        except Author.DoesNotExist:
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    @api_view(['PUT'])
    def update(request,id):
        try:
            author = Author.objects.get(id=id)
            serializer = AuthorSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create(request):
        try:
            author = Author()
            serializer = AuthorSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       
        
    @api_view(['DELETE'])
    def delete(request,id):
        try:
            author = Author.objects.get(id=id)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PublisherDAO:
    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            author = list(Publisher.objects.values())
            return JsonResponse(author, safe=False)
        except Publisher.DoesNotExist: 
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    @api_view(['GET'])
    def getById(request,id):
        try:
            author = Publisher.objects.get(id=id)
            return JsonResponse((PublisherSer(author).data), safe=False)
        except Publisher.DoesNotExist:
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    @api_view(['PUT'])
    def update(request,id):
        try:
            author = Publisher.objects.get(id=id)
            serializer = PublisherSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Publisher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create(request):
        try:
            author = Publisher()
            serializer = PublisherSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Publisher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       
        
    @api_view(['DELETE'])
    def delete(request,id):
        try:
            author = Publisher.objects.get(id=id)
        except Publisher.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryBookDAO:
    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            author = list(CategoryBook.objects.values())
            return JsonResponse(author, safe=False)
        except CategoryBook.DoesNotExist: 
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    @api_view(['GET'])
    def getById(request,id):
        try:
            author = CategoryBook.objects.get(id=id)
            return JsonResponse((CategoryBookSer(author).data), safe=False)
        except CategoryBook.DoesNotExist:
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    @api_view(['PUT'])
    def update(request,id):
        try:
            author = CategoryBook.objects.get(id=id)
            serializer = CategoryBookSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CategoryBook.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create(request):
        try:
            author = CategoryBook()
            serializer = CategoryBookSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CategoryBook.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       
        
    @api_view(['DELETE'])
    def delete(request,id):
        try:
            author = CategoryBook.objects.get(id=id)
        except CategoryBook.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookDAO:
    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            author = list(Book.objects.values())
            return JsonResponse(author, safe=False)
        except Book.DoesNotExist: 
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    @api_view(['GET'])
    def getById(request,id):
        try:
            author = Book.objects.get(id=id)
            return JsonResponse((BookSer(author).data), safe=False)
        except Book.DoesNotExist:
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    @api_view(['PUT'])
    def update(request,id):
        try:
            author = Book.objects.get(id=id)
            serializer = BookSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create(request):
        try:
            author = Book()
            serializer = BookSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       
        
    @api_view(['DELETE'])
    def delete(request,id):
        try:
            author = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BookItemDAO:
    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            author = list(BookItem.objects.values())
            return JsonResponse(author, safe=False)
        except BookItem.DoesNotExist: 
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    @api_view(['GET'])
    def getById(request,id):
        try:
            author = BookItem.objects.get(id=id)
            return JsonResponse((BookItemSer(author).data), safe=False)
        except BookItem.DoesNotExist:
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    @api_view(['PUT'])
    def update(request,id):
        try:
            author = BookItem.objects.get(id=id)
            serializer = BookItemSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except BookItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create(request):
        try:
            author = BookItem()
            serializer = BookItemSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except BookItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       
        
    @api_view(['DELETE'])
    def delete(request,id):
        try:
            author = BookItem.objects.get(id=id)
        except BookItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

