# Generated by Django 3.1.4 on 2021-01-18 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('script', '0002_auto_20210118_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Script',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('script', models.CharField(max_length=1000)),
            ],
        ),
    ]
