# Generated by Django 3.2.5 on 2021-07-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='creditform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cfrom', models.CharField(max_length=50)),
                ('camount', models.IntegerField()),
                ('cdate', models.DateField()),
                ('creason', models.CharField(max_length=100)),
                ('cmode', models.CharField(max_length=20)),
            ],
        ),
    ]