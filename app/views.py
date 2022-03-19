from django.shortcuts import render
from app.serializers import *
from .models import *
from rest_framework import viewsets

# Create your views here.


class CometitionViews(viewsets.ModelViewSet):
    serializer_class = CompetitionSerializer
    def get_queryset(self):
        return Competition.objects.all()


class ResultViews(viewsets.ModelViewSet):
    serializer_class = ResultSerializer
    def get_queryset(self):
        return Result.objects.all()

