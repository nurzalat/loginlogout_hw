# Generated by Django 3.2.7 on 2022-05-13 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='password',
            field=models.CharField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]