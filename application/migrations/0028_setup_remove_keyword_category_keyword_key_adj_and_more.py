# Generated by Django 4.2 on 2023-04-07 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0027_keyword_delete_productreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='keyword',
            name='category',
        ),
        migrations.AddField(
            model_name='keyword',
            name='key_adj',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='keyword',
            name='setup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.setup'),
        ),
    ]
