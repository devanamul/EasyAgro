# Generated by Django 4.0.4 on 2023-05-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyAgro', '0007_postplantingprocess_irrigation'),
    ]

    operations = [
        migrations.AddField(
            model_name='postplantingprocess',
            name='time',
            field=models.IntegerField(default=0),
        ),
    ]
