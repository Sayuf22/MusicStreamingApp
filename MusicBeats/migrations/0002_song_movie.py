# Generated by Django 3.2.2 on 2021-05-15 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MusicBeats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='movie',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
