# Generated by Django 3.0.6 on 2020-08-14 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='updates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=100)),
                ('date', models.IntegerField()),
                ('heading', models.TextField()),
                ('desc', models.TextField()),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
