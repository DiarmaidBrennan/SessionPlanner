# Generated by Django 3.0.7 on 2020-06-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=2000)),
                ('min_num_players', models.IntegerField(default=0)),
                ('max_number_players', models.IntegerField(default=0)),
                ('scaleability', models.IntegerField(default=0)),
            ],
        ),
    ]
