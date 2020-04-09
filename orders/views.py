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
        item = cartItems.objects.all().get(
            username=username, productID=productID, productType=productType)
        noOfProducts = getattr(item, "numOfProducts")
        noOfProducts += 1
        setattr(item, "numOfProducts", noOfProducts)
        item.save()

    except:
        item = cartItems(username=username, productID=productID,
                         productType=productType)
        noOfProducts = getattr(item, "numOfProducts")
        noOfProducts += 1
        setattr(item, "numOfProducts", noOfProducts)
        item.save()

    return redirect('orders:cart')


@login_required()
def cart(request):
    username = request.user.username
    userCartItemsInfo = cartItems.objects.all().filter(username=username)
    items = []
    for userCartItemInfo in userCartItemsInfo:
        productID = userCartItemInfo.productID
        productType = userCartItemInfo.productType
        numOfProduct = userCartItemInfo.numOfProducts
        item = []

        try:
            itemInfo = regularpizza.objects.all().get(productID=productID)
            itemName = getattr(itemInfo, "reg_pizza")
            itemPrice = '${:,.2f}'.format(getattr(itemInfo, productType))
            if productType == "reg_small_price":
                itemType = "S"
            else:
                itemType = "L"

            item.append("Regular Pizza")
            item.append(itemName)
            item.append(itemPrice)
            item.append(numOfProduct)
            item.append(itemType)
            items.append(item)
        except:
            pass

        try:
            itemInfo = sicilianpizza.objects.all().get(productID=productID)
            itemName = getattr(itemInfo, "sic_pizza")
            itemPrice = '${:,.2f}'.format(getattr(itemInfo, productType))
            if productType == "sic_small_price":
                itemType = "S"
            else:
                itemType = "L"

            item.append("Sicilian Pizza")
            item.append(itemName)
            item.append(itemPrice)
            item.append(numOfProduct)
            item.append(itemType)
            items.append(item)
        except:
            pass

        try:
            itemInfo = sub.objects.all().get(productID=productID)
            itemName = getattr(itemInfo, "sub_name")
            itemPrice = '${:,.2f}'.format(getattr(itemInfo, productType))
            if productType == "sic_small_price":
                itemType = "S"
            else:
                itemType = "L"

            item.append("Subs")
            item.append(itemName)
            item.append(itemPrice)
            item.append(numOfProduct)
            item.append(itemType)
            items.append(item)
        except:
            pass

        try:
            itemInfo = pasta.objects.all().get(productID=productID)
            itemName = getattr(itemInfo, "pasta_name")
            itemPrice = '${:,.2f}'.format(getattr(itemInfo, productType))

            item.append("Pasta")
            item.append(itemName)
            item.append(itemPrice)
            item.append(numOfProduct)
            items.append(item)
        except:
            pass

        try:
            itemInfo = salad.objects.all().get(productID=productID)
            itemName = getattr(itemInfo, "salad_name")
            itemPrice = '${:,.2f}'.format(getattr(itemInfo, productType))

            item.append("Salad")
            item.append(itemName)
            item.append(itemPrice)
            item.append(numOfProduct)
            items.append(item)
        except:
            pass

        try:
            itemInfo = dinner_platter.objects.all().get(productID=productID)
            itemInfo = sub.objects.all().get(productID=productID)
            itemName = getattr(itemInfo, "platter_name")
            itemPrice = '${:,.2f}'.format(getattr(itemInfo, productType))
            if productType == "platter_small_price":
                itemType = "S"
            else:
                itemType = "L"

            item.append("Dinner Platter")
            item.append(itemName)
            item.append(itemPrice)
            item.append(numOfProduct)
            item.append(itemType)
            items.append(item)
        except:
            pass

    context = {
        'userCartItems': items
    }

    return render(request, 'orders/cart.html', context)
