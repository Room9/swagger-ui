import json

from django.shortcuts import render
from django.http            import JsonResponse, HttpResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi



# Create your views here.


class PaymentReserverView(APIView):
    def post(self, request):
        # data = json.loads(request.body)
        return JsonResponse({'message':'KEY ERROR'}, status=400)

class PaymentStatusView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        return JsonResponse({'message':'KEY ERROR'}, status=400)

class PaymentApprovalView(APIView):
    def post(self, request):
        # data = json.loads(request.body)
        return JsonResponse({'message':'KEY ERROR'}, status=400)

class PaymentCancelView(APIView):
    def post(self, request):
        # data = json.loads(request.body)
        return JsonResponse({'message':'KEY ERROR'}, status=400)


class PaymentSttlinqView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        return JsonResponse({'message':'KEY ERROR'}, status=400)