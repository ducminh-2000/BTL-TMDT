from rest_framework import status
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from shop.serializers import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
class AuthorDAO:

    # pagination = CustomPagination()

    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            search = request.query_params.get('search') if request.query_params.get('search') != None else ""
            author = (Author.objects.filter(name__contains=search))
            res = list()
            for e in author:
                res.append(AuthorSer(e).data)
            return JsonResponse(res, safe=False)
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

@csrf_exempt
class PublisherDAO:
    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            search = request.query_params.get('search') if request.query_params.get('search') != None else ""
            author = (Publisher.objects.filter(name__contains=search))
            res = list()
            for e in author:
                res.append(PublisherSer(e).data)
            return JsonResponse(res, safe=False)
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

@csrf_exempt
class CategoryBookDAO:
    
    pagination = PageNumberPagination()
    
    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            search = request.query_params.get('search') if request.query_params.get('search') != None else ""
            author = list(CategoryBook.objects.filter(name__contains=search))
            res = list()
            for e in author:
                res.append(CategoryBookSer(e).data)
            return JsonResponse(res, safe=False)
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

@csrf_exempt
class BookDAO:

    # pagination = CustomPagination()
    
    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            search = request.query_params.get('search') if request.query_params.get('search') != None else ""
            author = (Book.objects.filter(title__contains=search))
            res = list()
            for e in author:
                res.append(BookSer(e).data)
            return JsonResponse(res, safe=False)
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

@csrf_exempt
class BookItemDAO:

    # pagination = CustomPagination()

    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            search = request.query_params.get('search') if request.query_params.get('search') != None else ""
            author = (BookItem.objects.filter(name__contains=search))
            res = list()
            for e in author:
                res.append(BookItemSer(e).data)
            return JsonResponse(res, safe=False)
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


@csrf_exempt
class CartDAO:

    # pagination = CustomPagination()

    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            author = (Cart.objects.filter())
            res = list()
            for e in author:
                res.append(CartSer(e).data)
            return JsonResponse(res, safe=False)
        except Cart.DoesNotExist: 
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    @api_view(['GET'])
    def getById(request,id):
        try:
            author = Cart.objects.get(id=id)
            return JsonResponse((CartSer(author).data), safe=False)
        except Cart.DoesNotExist:
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    @api_view(['PUT'])
    def update(request,id):
        try:
            author = Cart.objects.get(id=id)
            serializer = CartSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create(request):
        try:
            author = Cart()
            serializer = CartSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       
        
    @api_view(['DELETE'])
    def delete(request,id):
        try:
            author = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
class OrderDAO:

    # pagination = CustomPagination()

    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            author = (Order.objects.filter())
            res = list()
            for e in author:
                res.append(OrderSer(e).data)
            return JsonResponse(res, safe=False)
        except Order.DoesNotExist: 
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    @api_view(['GET'])
    def getById(request,id):
        try:
            author = Order.objects.get(id=id)
            return JsonResponse((CartSer(author).data), safe=False)
        except Order.DoesNotExist:
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    @api_view(['PUT'])
    def update(request,id):
        try:
            author = Order.objects.get(id=id)
            serializer = OrderSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create(request):
        try:
            author = Order()
            serializer = OrderSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       
        
    @api_view(['DELETE'])
    def delete(request,id):
        try:
            author = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
class CustomerDAO:

    # pagination = CustomPagination()

    @api_view(['GET'])
    def list(request):
        # find Author by pk (id)
        try: 
            author = (Customer.objects.filter())
            res = list()
            for e in author:
                res.append(CustomerSer(e).data)
            return JsonResponse(res, safe=False)
        except Customer.DoesNotExist: 
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    @api_view(['GET'])
    def getById(request,id):
        try:
            author = Customer.objects.get(id=id)
            return JsonResponse((CustomerSer(author).data), safe=False)
        except Customer.DoesNotExist:
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET'])
    def login(request):
        # find Author by pk (id)
        try: 
            username = request.query_params.get('username') if request.query_params.get('username') != None else ""
            password = request.query_params.get('password') if request.query_params.get('password') != None else ""
            account = Account.objects.filter(username__contains=username).filter(password__contains=password).get()
            if(account != None):
                author = (Customer.objects.filter(account_id=account.id))
                res = list()
                for e in author:
                    res.append(CustomerSer(e).data)
                return JsonResponse(res, safe=False)
            else:
                return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND) 

        except Customer.DoesNotExist: 
            return Response({'message': 'The Author does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    @api_view(['PUT'])
    def update(request,id):
        try:
            author = Customer.objects.get(id=id)
            serializer = CustomerSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @api_view(['POST'])
    def create(request):
        try:
            author = Customer()
            serializer = CustomerSer(author, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)       
        
    @api_view(['DELETE'])
    def delete(request,id):
        try:
            author = Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


