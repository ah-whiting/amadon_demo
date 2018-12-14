from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    price_from_form = float(request.POST["price"])
    print("Charging credit card...")
    total_charge = quantity_from_form * price_from_form
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/confirmed')

def confirmation(request):
    context = {
        'order': Order.objects.last(),
        'total_cost': Order.objects.aggregate(sum = Sum('total_price')),
        'total_quantity':Order.objects.aggregate(sum = Sum('quantity_ordered'))
    }
    return render(request, "store/checkout.html", context)