from rest_framework import serializers
from .models import *


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ['date']


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['compttion', 'user']


class ScrambleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scramble
        fields = ['item_333']