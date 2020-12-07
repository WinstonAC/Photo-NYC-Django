# Generated by Django 3.1.4 on 2020-12-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('photo_url', models.TextField()),
                ('loaction', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]
