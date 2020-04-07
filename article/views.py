from rest_framework.response import Response 
from article.serializers import ArticleSerializer
from .models import Article
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.core import serializers
from django.http import QueryDict
from rest_framework.request import Request

def show(request):
	articles=Article.objects.all()
	serializer=ArticleSerializer(articles,many=True)
	d=json.dumps(serializer.data)
	return HttpResponse(d)
@csrf_exempt
def addarticle(request):
	if request.method=="POST":
		print(request.POST)
	
		"""data=JSONParser().parse(BytesIO(request.data))
		a=request.body
		k=json.loads(a.decode('utf-8'))
		query_dict = QueryDict('', mutable=True)
		query_dict.update(k)
		print(query_dict)
		serializer=ArticleSerializer(data=query_dict)
		if serializer.is_valid():
			serializer.save()
			return HttpResponse(serializer.data,status=201)
		else:
			return HttpResponse(serializer.errors, status=400)"""
	"""a=request.body
	k=json.loads(a.decode('utf-8'))"""
		
	
	#j=json.dumps(request)
	return HttpResponse(request.POST)
		