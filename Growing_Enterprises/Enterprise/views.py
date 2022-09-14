from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm

from .models import Membership

# Create your views here.

def process_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Membership, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.total_cost().quantize(
            Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'MXN',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'Enterprise/process_payment.html', {'order': order, 'form': form})


@csrf_exempt
def payment_done(request):
    return render(request, 'Enterprise/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'Enterprise/payment_cancelled.html')
