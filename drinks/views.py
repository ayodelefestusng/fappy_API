
from django.http import JsonResponse, HttpResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from rest_framework import status
from rest_framework import response, status



@api_view(['GET','POST'])
def drink_list(request, format =None):
    if request.method=='GET' :
        drinks =Drink.objects.all()
        serializer = DrinkSerializer(drinks, many = True)
        # return JsonResponse(serializer.data, safe=False)
        # return JsonResponse({'drinks' :serializer.data}, safe=False)
        return Response(serializer.data)
        
    
    if request.method=='POST' :
        serializer= DrinkSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
    # Postman for tesing API 
    
@api_view(['GET','PUT', 'DELETE'])
def drink_detail(request, pk, format =None):
    try:
        drink =Drink.objects.get (pk=pk)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialiser =DrinkSerializer(drink)
        return Response(serialiser.data)
    elif request.method =='PUT':
        serialiser =DrinkSerializer(drink, data =request.data) 
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        return Response (serialiser.errors, status= status.HTTP_400_BAD_REQUEST )
    elif request.method == 'DELETE':
        drink.delete() 
        return Response(status= status.HTTP_204_NO_CONTENT)
    
    