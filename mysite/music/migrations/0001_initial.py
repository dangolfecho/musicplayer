# Generated by Django 4.0.6 on 2024-03-14 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_no', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('file_location', models.FilePathField()),
                ('duration', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=50)),
                ('song_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.song')),
            ],
        ),
    ]
