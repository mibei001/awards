# Generated by Django 4.0.5 on 2022-06-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='projects',
            name='screen_one',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='projects',
            name='screen_two',
            field=models.ImageField(upload_to=''),
        ),
    ]
