# Generated by Django 3.0.7 on 2020-06-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessionplanner', '0006_section_sports_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportssession',
            name='name',
            field=models.CharField(default='Session', max_length=20, verbose_name='Session Name'),
        ),
    ]
