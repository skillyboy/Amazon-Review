# Generated by Django 4.2 on 2023-04-06 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_review_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
