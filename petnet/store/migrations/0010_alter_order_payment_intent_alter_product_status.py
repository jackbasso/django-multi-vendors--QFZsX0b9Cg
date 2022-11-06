# Generated by Django 4.1.2 on 2022-11-05 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_intent',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('waitingapproval', 'Waiting approval'), ('draft', 'Draft'), ('deleted', 'Deleted')], default='active', max_length=50),
        ),
    ]