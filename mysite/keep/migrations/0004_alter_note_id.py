# Generated by Django 4.0.6 on 2024-03-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keep', '0003_alter_note_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
