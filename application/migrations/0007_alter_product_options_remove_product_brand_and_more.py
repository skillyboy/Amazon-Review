# Generated by Django 4.2 on 2023-04-06 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_product_overall_product_reviewtext_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'products'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='product',
            name='overall',
        ),
        migrations.RemoveField(
            model_name='product',
            name='related',
        ),
        migrations.RemoveField(
            model_name='product',
            name='reviewText',
        ),
        migrations.RemoveField(
            model_name='product',
            name='reviewTime',
        ),
        migrations.RemoveField(
            model_name='product',
            name='reviewerID',
        ),
        migrations.RemoveField(
            model_name='product',
            name='reviewerName',
        ),
        migrations.RemoveField(
            model_name='product',
            name='salesRank',
        ),
        migrations.RemoveField(
            model_name='product',
            name='similar',
        ),
        migrations.RemoveField(
            model_name='product',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tech1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tech2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='unixReviewTime',
        ),
        migrations.RemoveField(
            model_name='product',
            name='verified',
        ),
        migrations.RemoveField(
            model_name='review',
            name='helpfulness',
        ),
        migrations.RemoveField(
            model_name='review',
            name='overall_rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='product',
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_text',
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_time',
        ),
        migrations.RemoveField(
            model_name='review',
            name='reviewer_id',
        ),
        migrations.AddField(
            model_name='review',
            name='asin',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.category'),
        ),
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='overall',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewText',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewTime',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewerID',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='reviewerName',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='unixReviewTime',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='asin',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AlterField(
            model_name='rating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='style',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='summary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='verified',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='vote',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='application.category'),
        ),
    ]
