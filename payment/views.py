import json

from django.shortcuts     import render
from django.http          import JsonResponse, HttpResponse
from payment.models       import PaymentCancel, PaymentStatus, PaymentSttlinq, PaymentApproval, PaymentReserver

from rest_framework.views import APIView
from drf_yasg.utils       import swagger_auto_schema
from drf_yasg             import openapi


class PaymentReserverView(APIView):
    def post(self, request):
        data = PaymentReserver.objects.first()

        result= {
            "code": "000",
            "msg" : "성공",
            "data": {
            "tid"              : data.tid,
            "redirectURLPC"    : data.redirect_url_pc,
            "redirectURLMobile": data.redirect_url_mobile,
            "createdAt"        : data.created_at
            }
        }

        return JsonResponse(result, status=200)

class PaymentStatusView(APIView):
    def post(self, request):
        data = PaymentStatus.objects.first()

        result = {
            'code'         : '000',
            'msg'          : '성공',
            'data' : {
                "aid"            : data.aid,
                "tid"            : data.tid,
                "mid"            : data.mid,
                "status"         : data.status,
                "merchantOrderID": data.merchant_order_id,
                "merchantUserKey": data.merchant_user_key,
                "totalAmount"    : data.total_amount,
                "taxFreeAmount"  : data.tax_free_amount,
                "vatAmount"      : data.vat_amount,
                "canceledAmount" : data.canceled_amount,
                "productName"    : data.product_name,
                "quantity"       : data.quantity,
                "createdAt"      : data.created_at,
                "approvedAt"     : data.approved_at,
                "canceledAt"     : data.canceled_at
            }
        }

        return JsonResponse(result, status=200)

class PaymentApprovalView(APIView):
    def post(self, request):
        data = PaymentApproval.objects.first()

        result= {
            "code": "000",
            "msg" : "성공",
            "data": {
                "aid"            : data.aid,
                "tid"            : data.tid,
                "mid"            : data.mid,
                "merchantOrderID": data.merchant_order_id,
                "merchantUserKey": data.merchant_user_key,
                "totalAmount"    : data.total_amount,
                "taxFreeAmount"  : data.tax_free_amount,
                "vatAmount"      : data.vat_amount,
                "productName"    : data.product_name,
                "payload"        : data.payload,
                "quantity"       : data.quantity,
                "createdAt"      : data.created_at,
                "approvedAt"     : data.approved_at
            }
        }

        return JsonResponse(result, status=200)

class PaymentCancelView(APIView):
    def post(self, request):
        data = PaymentCancel.objects.first()

        result = {
            'code': '000',
            'msg': '성공',
            'data': {
                'aid'            : data.aid,
                'tid'            : data.tid,
                'mid'            : data.mid,
                'status'         : data.status,
                'merchantOrderID': data.merchant_order_id,
                'merchantUserKey': data.merchant_user_key,
                'totalAmount'    : data.total_amount,
                'canceledAmount' : data.canceled_amount,
                'productName'    : data.product_name,
                'quantity'       : data.quantity,
                'createdAt'      : data.created_at,
                'approvedAt'     : data.approved_at,
                'canceledAt'     : data.canceled_at,
                'payload'        : data.payload
            }
        }

        return JsonResponse(result, status=200)

class PaymentSttlinqView(APIView):
    def post(self, request):
        data = PaymentSttlinq.objects.first()

        result = {
            'code'         : '000',
            'msg'          : '성공',
            'nextPageIndex': data.nextPageIndex,
            'data' : {
                "mid"              : data.mid,
                "zpid"             : data.zpid,
                "stStartDate"      : data.st_start_date,
                "stEndDate"        : data.st_end_date,
                "payCount"         : data.pay_count,
                "payAmount"        : data.pay_amount,
                "cclCount"         : data.ccl_count,
                "cclAmount"        : data.ccl_amount,
                "tgtCount"         : data.tgt_count,
                "tgtAmount"        : data.tgt_amount,
                "commRate"         : data.comm_rate,
                "commission"       : data.commision,
                "vatAmount"        : data.vat_amount,
                "slTerm"           : data.sl_term,
                "slAmount"         : data.sl_amount,
                "slMinusAmt"       : data.sl_minus_amt,
                "slTransferredDate": data.sl_transfered_date,
                "slTransferStatus" : data.sl_transfer_status,
                "slTransferredAmt" : data.sl_transfer_amt,
                "inBankName"       : data.inBankName,
                "inAcctNo"         : data.inAcctNo,
                "inOwnerName"      : data.inOwnerName,
            }
        }

        return JsonResponse(result, status=200)