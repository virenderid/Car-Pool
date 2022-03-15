# Generated by Django 3.2 on 2022-03-15 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ride',
            fields=[
                ('userId', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('pickUp', models.CharField(max_length=200)),
                ('destination', models.CharField(max_length=200)),
                ('complete', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=False)),
                ('cost', models.PositiveIntegerField(default=0)),
                ('driverId', models.CharField(default=None, max_length=200, null=True)),
                ('expectedTime', models.CharField(default='inf', max_length=200)),
            ],
        ),
    ]
