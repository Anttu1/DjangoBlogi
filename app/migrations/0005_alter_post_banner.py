# Generated by Django 4.2.16 on 2024-09-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_post_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='banner',
            field=models.ImageField(blank=True, default='empty.jpg', upload_to=''),
        ),
    ]
