from django.urls import path

from payment.views import PaymentReserverView,PaymentApprovalView,PaymentCancelView,PaymentStatusView,PaymentSttlinqView

urlpatterns = [
    path('api_v1_payment_reserve.jct', PaymentReserverView.as_view()),
    path('api_v1_payment_approval.jct', PaymentApprovalView.as_view()),
    path('api_v1_payment_cancel.jct', PaymentCancelView.as_view()),
    path('api_v1_payment_status.jct', PaymentStatusView.as_view()),
    path('api_v1_payment_sttlinq.jct', PaymentSttlinqView.as_view()),
]