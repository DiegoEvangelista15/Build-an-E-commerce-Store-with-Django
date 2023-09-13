from django.shortcuts import render
from .models import ShippingAddress

# Create your views here.

def checkout(request):
    # Users with account -- Prefill de form
    if request.user.is_authenticated:
        try:
            #authenticated user with shipping information
            shipping_address = ShippingAddress.objects.get(user=request.user.id)
            context = {'shipping': shipping_address}
            return render(request, 'payment/checkout.html', context=context)
        except:
            # authenticated user with NO shipping information
            return render(request, 'payment/checkout.html')
        # GUEST user
    return render (request, 'payment/checkout.html')

def payment_success(request):
    return render(request, 'payment/payment-success.html')
    
def payment_failed(request):
    return render(request, 'payment/payment-failed.html')