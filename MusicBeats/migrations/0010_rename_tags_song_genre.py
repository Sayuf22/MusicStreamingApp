# Generated by Django 3.2.2 on 2021-05-19 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MusicBeats', '0009_alter_song_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='tags',
            new_name='genre',
        ),
    ]
