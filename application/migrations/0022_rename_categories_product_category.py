# Generated by Django 4.2 on 2023-04-07 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0021_alter_review_asin_alter_review_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='category',
        ),
    ]
