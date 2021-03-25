from django.db import models


# ORM, 类-表， 属性-字段，实例-记录
class User(models.Model):
    name = models.CharField('名字', max_length=32)
