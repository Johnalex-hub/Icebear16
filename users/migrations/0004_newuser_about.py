# Generated by Django 3.2.4 on 2021-06-29 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210629_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='about',
            field=models.TextField(blank=True, max_length=500, verbose_name='about'),
        ),
    ]
