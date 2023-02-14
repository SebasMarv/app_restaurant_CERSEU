# Generated by Django 4.1.6 on 2023-02-14 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('position', models.CharField(default='', max_length=40)),
                ('years', models.IntegerField()),
            ],
        ),
    ]