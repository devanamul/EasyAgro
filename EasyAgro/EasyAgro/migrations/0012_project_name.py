# Generated by Django 4.0.4 on 2023-05-01 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EasyAgro', '0011_remove_postplantingprocess_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
    ]