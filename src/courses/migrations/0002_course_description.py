# Generated by Django 3.1.5 on 2021-01-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]