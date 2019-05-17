# Generated by Django 2.2.1 on 2019-05-08 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sf', '0002_auto_20190508_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.BigIntegerField(default=0, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.IntegerField(default=0, help_text='0:普通用户，1：管理员', verbose_name='类型'),
        ),
    ]
