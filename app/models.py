from django.db import models

# Create your models here.

class Classmate(models.Model):
    name = models.CharField('姓名', max_length=10)
    school = models.CharField('学校', max_length=20)
    major = models.CharField('专业', max_length=20, default='')
    
    class Meta:
        ordering = ('school', 'major',)
    
    def __str__(self):
        return self.name + ':    ' + self.school + '    ' + self.major