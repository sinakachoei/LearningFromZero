# Generated by Django 2.1.4 on 2019-01-02 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20190102_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='SID',
        ),
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]