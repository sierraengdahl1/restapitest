from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import action
from rest_framework import viewsets
from django.db.models import Count
from rest_framework.response import Response
from django.http import HttpResponse
import json

from .serializers import InputSerializer
from .models import Input


class InputViewSet(viewsets.ModelViewSet):
    queryset = Input.objects.all().order_by('name')
    serializer_class = InputSerializer
''' def get_queryset(self) :
        user = self.request.user
        return Input.objects.filter(name=user)

    @action(detail=False)
    def count(name, message):
        queryset = Input.objects.annotate(Count('name'), Count('message'))
        my_list = list(queryset.get_queryset().values_list('code', flat=True))
        json_data = json.dumps(my_list)
        response = HttpResponse(json_data, content_type='application/json')
        return response
        #queryset = Input.objects.all()
        #return Response(queryset)
        #return HttpResponse(json.dumps(queryset), mimetype="application/json")
        

    #def get_permissions(self):
        #if self.action in ('count'):
            #return (AllowAny()),
        #if self.action in ('update', 'partial_update'):
            #return (IsAdminUser()),
        #return (IsAdminUser()),

    @action(detail=False)
    def count(self, request):
        queryset = Input.objects.annotate(Count('name'), Count('message'))
        #count = queryset.count()
        #content = {'count': queryset}
        HttpResponse(json.simplejson.dumps(queryset), mimetype="application/json")
'''
