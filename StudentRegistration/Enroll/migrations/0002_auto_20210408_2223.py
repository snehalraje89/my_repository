# Generated by Django 3.1.7 on 2021-04-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Enroll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
