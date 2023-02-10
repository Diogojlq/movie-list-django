# Generated by Django 4.1.3 on 2023-02-08 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='watched',
        ),
        migrations.AddField(
            model_name='movie',
            name='comment',
            field=models.CharField(default='Enter a comment', max_length=30),
        ),
    ]
