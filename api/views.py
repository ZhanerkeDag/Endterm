from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from main.models import Person, Achievements, Category
from api.serializers import PersonModelSerializer, CategoryModelSerializer, AchievementsModelSerializer

app_name = 'api'

@api_view(['POST'])
def login(request):
	username = request.data.get('username')
	password = request.data.get('password')
	user = authenticate(username=username, password=password)
	if user is None:
		return Response({'error': 'Invalid data'})
	token, created = Token.objects.get_or_create(user=user)
	return Response({'token': token.key})
@api_view(['GET', 'POST'])
@csrf_exempt
def persons_list(request):
    if request.method=='GET':
        persons = Person.objects.all()
        serializer = PersonModelSerializer(persons, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST' and request.META.get('HTTP_AUTHORIZATION'):
        data = JSONParser().parse(request)
        serializer = PersonModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def persons_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = PersonModelSerializer(person)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT' and request.META.get('HTTP_AUTHORIZATION'):
        data = JSONParser().parse(request)
        serializer = PersonModelSerializer(person, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE' and request.META.get('HTTP_AUTHORIZATION'):
        person.delete()
        return HttpResponse(status=204)
@api_view(['GET', 'POST'])
@csrf_exempt
def categories_list(request):
	if request.method == 'GET':
		categories = Category.objects.all()
		serializer = CategoryModelSerializer(categories, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST' and request.META.get('HTTP_AUTHORIZATION'):
		data = JSONParser().parse(request)
		serializer = CategoryModelSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def categories_detail(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = CategoryModelSerializer(category)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT' and request.META.get('HTTP_AUTHORIZATION'):
        data = JSONParser().parse(request)
        serializer = CategoryModelSerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE' and request.META.get('HTTP_AUTHORIZATION'):
        category.delete()
        return HttpResponse(status=204)
@api_view(['GET', 'POST'])
@csrf_exempt
def achievements_list(request):
	if request.method == 'GET':
		achievements = Achievements.objects.all()
		serializer = AchievementsModelSerializer(achievements, many=True)
		return JsonResponse(serializer.data, safe=False)
	elif request.method == 'POST' and request.META.get('HTTP_AUTHORIZATION'):
		data = JSONParser().parse(request)
		serializer = AchievementsModelSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)
@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def achievements_detail(request, pk):
    try:
        achievements = Achievements.objects.get(pk=pk)
    except Achievements.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = AchievementsModelSerializer(achievements)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT' and request.META.get('HTTP_AUTHORIZATION'):
        data = JSONParser().parse(request)
        serializer = AchievementsModelSerializer(achievements, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE' and request.META.get('HTTP_AUTHORIZATION'):
        achievements.delete()
        return HttpResponse(status=204)
