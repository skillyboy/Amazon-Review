# Generated by Django 4.2 on 2023-04-06 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_alter_review_asin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='asin',
        ),
    ]
