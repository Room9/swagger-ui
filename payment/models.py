from django.db import models

class PaymentReserver(models.Model):
    tid                 = models.CharField(max_length=20)
    redirect_url_pc     = models.CharField(max_length=255)
    redirect_url_mobile = models.CharField(max_length=255)
    created_at          = models.CharField(max_length=20)

    class Meta:
        db_table = 'payment_reserver'

class PaymentStatus(models.Model):
    aid               = models.CharField(max_length=20)
    tid               = models.CharField(max_length=20)
    mid               = models.CharField(max_length=12)
    status            = models.CharField(max_length=20)
    merchant_order_id = models.CharField(max_length=100)
    merchant_user_key = models.CharField(max_length=100)
    total_amount      = models.DecimalField(max_digits=12, decimal_places=0)
    product_name      = models.CharField(max_length=100)
    quantity          = models.DecimalField(max_digits=10, decimal_places=0)
    created_at        = models.CharField(max_length=17)
    approved_at       = models.CharField(max_length=17)
    tax_free_amount   = models.DecimalField(max_digits=12, decimal_places=0)
    vat_amount        = models.DecimalField(max_digits=12, decimal_places=0)
    canceled_amount   = models.DecimalField(max_digits=12, decimal_places=0)
    canceled_at       = models.CharField(max_length=17)

    class Meta:
        db_table = 'payment_status'

class PaymentApproval(models.Model):
    aid               = models.CharField(max_length=20)
    tid               = models.CharField(max_length=20)
    mid               = models.CharField(max_length=12)
    merchant_order_id = models.CharField(max_length=100)
    merchant_user_key = models.CharField(max_length=100)
    total_amount      = models.DecimalField(max_digits=12, decimal_places=0)
    product_name      = models.CharField(max_length=100)
    quantity          = models.DecimalField(max_digits=10, decimal_places=0)
    created_at        = models.CharField(max_length=17)
    approved_at       = models.CharField(max_length=17)
    tax_free_amount   = models.DecimalField(max_digits=12, decimal_places=0)
    vat_amount        = models.DecimalField(max_digits=12, decimal_places=0)
    payload           = models.CharField(max_length=255)

    class Meta:
        db_table = 'payment_approval'

class PaymentCancel(models.Model):
    aid               = models.CharField(max_length=20)
    tid               = models.CharField(max_length=20)
    mid               = models.CharField(max_length=12)
    status            = models.CharField(max_length=20)
    merchant_order_id = models.CharField(max_length=100)
    merchant_user_key = models.CharField(max_length=100)
    total_amount      = models.DecimalField(max_digits=12, decimal_places=0)
    product_name      = models.CharField(max_length=100)
    quantity          = models.DecimalField(max_digits=10, decimal_places=0)
    payload           = models.CharField(max_length=255)
    created_at        = models.CharField(max_length=17)
    approved_at       = models.CharField(max_length=17)
    canceled_amount   = models.DecimalField(max_digits=12, decimal_places=0)
    canceled_at       = models.CharField(max_length=17)

    class Meta:
        db_table = 'payment_cancel'

class PaymentSttlinq(models.Model):
    nextPageIndex      = models.IntegerField()
    mid                = models.CharField(max_length=12)
    zpid               = models.CharField(max_length=12)
    st_start_date      = models.CharField(max_length=8)
    st_end_date        = models.CharField(max_length=8)
    pay_count          = models.DecimalField(max_digits=8, decimal_places=0)
    pay_amount         = models.DecimalField(max_digits=13, decimal_places=0)
    ccl_count          = models.DecimalField(max_digits=8, decimal_places=0)
    ccl_amount         = models.DecimalField(max_digits=13, decimal_places=0)
    tgt_count          = models.DecimalField(max_digits=8, decimal_places=0)
    tgt_amount         = models.DecimalField(max_digits=13, decimal_places=0)
    comm_rate          = models.DecimalField(max_digits=5, decimal_places=0)
    commision          = models.DecimalField(max_digits=13, decimal_places=0)
    vat_amount         = models.DecimalField(max_digits=13, decimal_places=0)
    sl_term            = models.CharField(max_length=5)
    sl_amount          = models.DecimalField(max_digits=13, decimal_places=0)
    sl_minus_amt       = models.DecimalField(max_digits=13, decimal_places=0)
    sl_transfer_status = models.CharField(max_length=1)
    sl_transfered_date = models.CharField(max_length=8)
    sl_transfer_amt    = models.DecimalField(max_digits=13, decimal_places=0)
    inBankName         = models.CharField(max_length=50)
    inAcctNo           = models.CharField(max_length=20)
    inOwnerName        = models.CharField(max_length=20)

    class Meta:
        db_table = 'payment_sttlinq'