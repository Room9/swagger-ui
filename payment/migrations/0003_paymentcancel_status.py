# Generated by Django 3.2.6 on 2021-08-24 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_paymentstatus_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentcancel',
            name='status',
            field=models.CharField(default='SUCCESS_PAYMENT', max_length=20),
            preserve_default=False,
        ),
    ]
