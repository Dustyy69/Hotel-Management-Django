# Generated by Django 4.2.4 on 2023-12-25 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_room_room_image1_room_room_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
