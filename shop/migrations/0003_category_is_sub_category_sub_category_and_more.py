# Generated by Django 4.0.5 on 2022-07-03 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_options_product_publish_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_sub',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scategory', to='shop.category'),
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='shop.category'),
        ),
    ]