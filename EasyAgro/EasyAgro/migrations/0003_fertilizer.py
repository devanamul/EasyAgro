# Generated by Django 4.0.4 on 2023-04-08 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EasyAgro', '0002_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nitrogen', models.FloatField()),
                ('phosphorous', models.FloatField()),
                ('potassium', models.FloatField()),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EasyAgro.crops')),
            ],
        ),
    ]
