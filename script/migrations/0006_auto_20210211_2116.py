# Generated by Django 3.1.4 on 2021-02-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('script', '0005_auto_20210211_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='LuaScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.FileField(default='', upload_to='Files')),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='scriptName',
            field=models.CharField(default='', max_length=15),
        ),
    ]
