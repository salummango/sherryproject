# Generated by Django 4.1.5 on 2023-01-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('Passenger_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Passenger_address', models.CharField(max_length=50)),
                ('Passenger_phonenumber', models.IntegerField()),
            ],
        ),
    ]
