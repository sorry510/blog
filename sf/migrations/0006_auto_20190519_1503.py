# Generated by Django 2.2.1 on 2019-05-19 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sf', '0005_articlecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecategory',
            name='is_show',
            field=models.IntegerField(default=0, help_text='0:显示，1：不显示', verbose_name='是否显示'),
        ),
        migrations.AddField(
            model_name='articlecategory',
            name='order',
            field=models.IntegerField(default=0, help_text='越小级别越高', verbose_name='排序'),
        ),
    ]