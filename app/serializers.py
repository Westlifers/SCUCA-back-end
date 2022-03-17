from rest_framework import serializers
from .models import *

class ClassmateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classmate
        fields = ["name", "school", "major"]