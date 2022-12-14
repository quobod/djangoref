# Generated by Django 4.0.5 on 2022-09-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('isadmin', models.BooleanField(default=False)),
                ('isvisible', models.BooleanField(default=False)),
                ('issignedin', models.BooleanField(default=False)),
                ('showemail', models.BooleanField(default=False)),
                ('showfullname', models.BooleanField(default=False)),
                ('passwordsaved', models.BooleanField(default=False)),
                ('creationdate', models.DateTimeField(auto_now=True)),
                ('resetToken', models.CharField(max_length=255)),
                ('expireToken', models.CharField(max_length=255)),
            ],
        ),
    ]
