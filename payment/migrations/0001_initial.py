# Generated by Django 3.2.6 on 2021-08-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentApproval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.CharField(max_length=20)),
                ('tid', models.CharField(max_length=20)),
                ('mid', models.CharField(max_length=12)),
                ('merchant_order_id', models.CharField(max_length=100)),
                ('merchant_user_key', models.CharField(max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=0, max_digits=12)),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=10)),
                ('created_at', models.CharField(max_length=17)),
                ('approved_at', models.CharField(max_length=17)),
                ('tax_free_amount', models.DecimalField(decimal_places=0, max_digits=12)),
                ('vat_amount', models.DecimalField(decimal_places=0, max_digits=12)),
                ('payload', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'payment_approval',
            },
        ),
        migrations.CreateModel(
            name='PaymentCancel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.CharField(max_length=20)),
                ('tid', models.CharField(max_length=20)),
                ('mid', models.CharField(max_length=12)),
                ('merchant_order_id', models.CharField(max_length=100)),
                ('merchant_user_key', models.CharField(max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=0, max_digits=12)),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=10)),
                ('payload', models.CharField(max_length=255)),
                ('created_at', models.CharField(max_length=17)),
                ('approved_at', models.CharField(max_length=17)),
                ('canceled_amount', models.DecimalField(decimal_places=0, max_digits=12)),
                ('canceled_at', models.CharField(max_length=17)),
            ],
            options={
                'db_table': 'payment_cancel',
            },
        ),
        migrations.CreateModel(
            name='PaymentReserver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(max_length=20)),
                ('redirect_url_pc', models.CharField(max_length=255)),
                ('redirect_url_mobile', models.CharField(max_length=255)),
                ('created_at', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'payment_reserver',
            },
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.CharField(max_length=20)),
                ('tid', models.CharField(max_length=20)),
                ('mid', models.CharField(max_length=12)),
                ('merchant_order_id', models.CharField(max_length=100)),
                ('merchant_user_key', models.CharField(max_length=100)),
                ('total_amount', models.DecimalField(decimal_places=0, max_digits=12)),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=10)),
                ('created_at', models.CharField(max_length=17)),
                ('approved_at', models.CharField(max_length=17)),
                ('tax_free_amount', models.DecimalField(decimal_places=0, max_digits=12)),
                ('vat_amount', models.DecimalField(decimal_places=0, max_digits=12)),
                ('canceled_amount', models.DecimalField(decimal_places=0, max_digits=12)),
                ('canceled_at', models.CharField(max_length=17)),
            ],
            options={
                'db_table': 'payment_status',
            },
        ),
        migrations.CreateModel(
            name='PaymentSttlinq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nextPageIndex', models.IntegerField()),
                ('mid', models.CharField(max_length=12)),
                ('zpid', models.CharField(max_length=12)),
                ('st_start_date', models.CharField(max_length=8)),
                ('st_end_date', models.CharField(max_length=8)),
                ('pay_count', models.DecimalField(decimal_places=0, max_digits=8)),
                ('pay_amount', models.DecimalField(decimal_places=0, max_digits=13)),
                ('ccl_count', models.DecimalField(decimal_places=0, max_digits=8)),
                ('ccl_amount', models.DecimalField(decimal_places=0, max_digits=13)),
                ('tgt_count', models.DecimalField(decimal_places=0, max_digits=8)),
                ('tgt_amount', models.DecimalField(decimal_places=0, max_digits=13)),
                ('comm_rate', models.DecimalField(decimal_places=0, max_digits=5)),
                ('commision', models.DecimalField(decimal_places=0, max_digits=13)),
                ('vat_amount', models.DecimalField(decimal_places=0, max_digits=13)),
                ('sl_term', models.CharField(max_length=5)),
                ('sl_amount', models.DecimalField(decimal_places=0, max_digits=13)),
                ('sl_minus_amt', models.DecimalField(decimal_places=0, max_digits=13)),
                ('sl_transfer_status', models.CharField(max_length=1)),
                ('sl_transfered_date', models.CharField(max_length=8)),
                ('sl_transfer_amt', models.DecimalField(decimal_places=0, max_digits=13)),
                ('inBankName', models.CharField(max_length=50)),
                ('inAcctNo', models.CharField(max_length=20)),
                ('inOwnerName', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'payment_sttlinq',
            },
        ),
    ]
