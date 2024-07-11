# Generated by Django 3.2.5 on 2021-07-31 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0003_rename_credit_creditform'),
    ]

    operations = [
        migrations.CreateModel(
            name='debitform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dfor', models.CharField(max_length=50)),
                ('damount', models.IntegerField()),
                ('ddate', models.DateField()),
                ('dreason', models.CharField(max_length=20)),
                ('dmode', models.CharField(max_length=20)),
                ('ddet', models.CharField(max_length=100)),
            ],
        ),
    ]
