# Generated by Django 3.2.2 on 2021-05-30 14:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MusicBeats', '0010_rename_tags_song_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('fav_id', models.AutoField(primary_key=True, serialize=False)),
                ('fav_song_id', models.CharField(default='', max_length=100000000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]