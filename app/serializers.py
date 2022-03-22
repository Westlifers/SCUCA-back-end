from numpy import source
from rest_framework import serializers
from .models import *


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ['date', 'item_222', 'item_333', 'item_444', 'item_555', 'item_666', 'item_777']


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ['competition', 'username', 'item', 'time1', 'time2', 'time3', 'time4', 'time5', 'video']
    
    username = serializers.CharField(source='user.username')
    def get_username(self, obj):
        return obj.user.username
