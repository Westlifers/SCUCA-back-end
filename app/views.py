from django.shortcuts import render
from app.serializers import ClassmateSerializer
from .models import *
from rest_framework import viewsets, mixins

# Create your views here.

class ClassmateViews(viewsets.ModelViewSet):
    serializer_class = ClassmateSerializer
    def get_queryset(self):
        return Classmate.objects.all()