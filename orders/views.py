from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import regularpizza, sicilianpizza, topping, sub, pasta, salad, dinner_platter, cartItems

# Create your views here.
@login_required()
def index(request):
    return render(request, 'orders/index.html')


@login_required()
def menu0(request):
    context = {
        'regularpizza_list': regularpizza.objects.all(),
        'toppings_list': topping.objects.all()
    }
    return render(request, 'orders/regularpizza.html', context)


@login_required()
def menu1(request):
    context = {
        'sicilianpizza_list': sicilianpizza.objects.all(),
        'toppings_list': topping.objects.all()
    }
    return render(request, 'orders/sicilianpizza.html', context)


@login_required()
def menu2(request):
    context = {
        'sub_list': sub.objects.all()
    }
    return render(request, 'orders/sub.html', context)


@login_required()
def menu3(request):
    context = {
        'pasta_list': pasta.objects.all()
    }
    return render(request, 'orders/pasta.html', context)


@login_required()
def menu4(request):
    context = {
        'salad_list': salad.objects.all()
    }
    return render(request, 'orders/salad.html', context)


@login_required()
def menu5(request):
    context = {
        'dinner_platter_list': dinner_platter.objects.all()
    }
    return render(request, 'orders/dinner_platter.html', context)


@login_required()
def addToCart(request):
    productInfo = request.POST["productInfo"]
    productInfoList = productInfo.split()
    productID = productInfoList[0]
    productType = productInfoList[1]
    username = request.user.username

    try:
        item = cartItems.objects.all().filter(
            username=username, productID=productID, productType=productType)
        item.numOfProducts += 1
        item.save()
    except:
        item = cartItems(username=username, productID=productID,
                         productType=productType)
        item.numOfProducts += 1
        item.save()

    return redirect('orders:cart')


@login_required()
def cart(request):
    username = request.user.username
    userCartItemsInfo: cartItems.objects.all().filter(username=username)
    items = ""

    return render(request, 'orders/cart.html')
