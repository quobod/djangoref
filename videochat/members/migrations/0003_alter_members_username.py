# Generated by Django 4.1.1 on 2022-09-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_members_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]