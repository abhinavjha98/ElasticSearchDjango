from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests
import json
from home.models import *

from .documents import *
from .serializers import *
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
import requests
from bs4 import BeautifulSoup
from .models import Url

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    OrderingFilterBackend,
)

def generate_random_data(query):
    url = 'https://newsapi.org/v2/everything?q='+query+'&from=2021-04-24&sortBy=publishedAt&apiKey=d4f421493e8241fa96a379a795ed4422'
    r = requests.get(url)
    payload = json.loads(r.text)
    count = 1
    for data in payload.get('articles'):
        print(count)
        ElasticDemo.objects.create(
            title = data.get('title'),
            content = data.get('description')
        )

def get_data():
        URL = 'https://db.aa419.org/fakebankslist.php'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        url_list = []
        j=0
        while(j<60):
            if j<60:
                URL = 'https://db.aa419.org/fakebankslist.php?start='+str(j)
                page = requests.get(URL)
                soup = BeautifulSoup(page.content, 'html.parser')
                tablerow = soup.find_all('tr', class_='ewTableRow')
                table_alt_row = soup.find_all('tr', class_='ewTableAltRow')
                
                tablerow = table_alt_row + tablerow
                for i in tablerow:
                    for link in i.find_all('a', href=True):
                        if "http" in link['href']:
                            print(link['href'])
                            if Url.objects.filter(url=link['href']).exists():
                                return Response(data={'status': 'Completed'}, status=status.HTTP_200_OK)
                            dbaa419 = Url(
                                url = link['href'],
                                label = 'bad'
                            )
                            dbaa419.save()
                            url_list.append(link['href'])
                j+=20
        return Response(data={'status': 'Completed'}, status=status.HTTP_200_OK)
def index(request):
    generate_random_data(query='microsoft')
    generate_random_data(query='apple')
    generate_random_data(query='google')
    generate_random_data(query='bitcoin')
    generate_random_data(query='india')
    generate_random_data(query='china')
    generate_random_data(query='us')
    get_data()
    return JsonResponse({'status' : 200})




class PublisherDocumentView(DocumentViewSet):
    document = NewsDocument
    serializer_class = NewsDocumentSerializer
    lookup_field = 'first_name'
    fielddata=True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
   
    search_fields = (
        'title',
        'content',
    )
    multi_match_search_fields = (
       'title',
        'content',
    )
    filter_fields = {
       'title' : 'title',
        'content' : 'content',
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ( 'id'  ,)

class UrlDocumentView(DocumentViewSet):
    document = UrlDocument
    serializer_class = UrlDocumentSerializer
    lookup_field = 'first_name'
    fielddata=True
    filter_backends = [
        FilteringFilterBackend,
        OrderingFilterBackend,
        CompoundSearchFilterBackend,
    ]
   
    search_fields = (
        'url',
        'label',
    )
    multi_match_search_fields = (
       'url',
        'label',
    )
    filter_fields = {
       'url' : 'url',
        'label' : 'label',
    }
    ordering_fields = {
        'id': None,
    }
    ordering = ( 'id'  ,)
        
  

