# Generated by Django 2.0.2 on 2021-12-12 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coats', '0002_auto_20211208_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=200)),
                ('total', models.CharField(max_length=200)),
            ],
        ),
    ]
