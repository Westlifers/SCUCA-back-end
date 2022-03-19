from email.policy import default
from django.db.models.deletion import CASCADE
from django.db import models
from django.contrib.auth.models import User
from .scrambler import *

# Create your models here.


""" 周赛表单，包含：次数，各项目打乱 """
class Competition(models.Model):
    date = models.AutoField(primary_key=True)
    item_222 = models.JSONField('222', default=scrambler)
    item_333 = models.JSONField('333', default=scrambler)
    item_444 = models.JSONField('444', default=scrambler)
    item_555 = models.JSONField('555', default=scrambler)
    item_666 = models.JSONField('666', default=scrambler)
    item_777 = models.JSONField('777', default=scrambler)

    def __str__(self) :
        return '第' + str(self.date) + '次周赛'



""" 成绩表单，包含：五次/三次成绩，指向一个用户和一个周赛 """
class Result(models.Model):
    competition = models.ForeignKey(Competition, on_delete=CASCADE)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True) # null = True是因为也许会支持匿名玩家
    items = (
        ('222', '222'),
        ('333', '333'),
        ('444', '444'),
        ('555', '555'),
        ('666', '666'),
        ('777', '777'),
        ('sk', 'sk'),
        ('py', 'py'),
        ('sq1', 'sq1'),
        ('minx', 'minx'),
        ('clock', 'clock'),
        ('FMC', 'FMC'),
        ('333oh', '333oh'),
        ('333bf', '333bf'),
        ('444bf', '444bf'),
        ('555bf', '555bf')
    )
    item = models.CharField('参赛项目', choices=items, max_length=10, default='333')
    time1 = models.FloatField('时间1', default=0.0)
    time2 = models.FloatField('时间2', default=0.0)
    time3 = models.FloatField('时间3', default=0.0)
    time4 = models.FloatField('时间4', default=0.0, blank=True, null=True)
    time5 = models.FloatField('时间5', default=0.0, blank=True, null=True)

