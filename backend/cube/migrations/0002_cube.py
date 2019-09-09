# Generated by Django 2.2.4 on 2019-09-08 21:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cube', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cube',
            fields=[
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('positions', models.CharField(default='yyyyyyyyybbbbbbbbbrrrrrrrrrgggggggggooooooooowwwwwwwww', max_length=54)),
            ],
        ),
    ]