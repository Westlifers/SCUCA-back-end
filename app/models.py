from email.policy import default
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User
from random import randint

# Create your models here.


class Classmate(models.Model):
    name = models.CharField('姓名', max_length=10)
    school = models.CharField('学校', max_length=20)
    major = models.CharField('专业', max_length=20, default='')
    
    class Meta:
        ordering = ('school', 'major',)
    
    def __str__(self):
        return self.name + ':    ' + self.school + '    ' + self.major


class Competition(models.Model):
    date = models.AutoField(primary_key=True)


class Scramble(models.Model):
    item_333 = models.JSONField('333', default=['asdwadawdawd', randint(1, 10)])


class Result(models.Model):
    competition = models.ForeignKey(Competition, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE)

