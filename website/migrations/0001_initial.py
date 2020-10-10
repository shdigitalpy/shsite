# Generated by Django 3.1.2 on 2020-10-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_name', models.CharField(max_length=255)),
                ('message_surname', models.CharField(max_length=255)),
                ('message_email', models.EmailField(max_length=255, unique=True)),
                ('message_phone', models.IntegerField()),
                ('message_body', models.CharField(max_length=1000)),
            ],
        ),
    ]
