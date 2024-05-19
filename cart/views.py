from django.contrib import messages
from django.shortcuts import render, redirect

from shop.models import Product
from .models import Favorite, Cart


def add_to_favorites(request, pk):
    user = request.user
    product = Product.objects.get(id=pk)

    favorite = Favorite.objects.create(
        user=user,
        product=product
    )

    favorite.save()
    messages.success(request, "Added to favorite!")
    return redirect('product_detail', pk)


def remove_from_favorites(request, pk):
    Favorite.objects.get(product=pk).delete()
    messages.error(request, 'Delete from Fav!')
    return redirect('product_detail', pk)


def favorites_list(request):
    favorites = Favorite.objects.filter(user=request.user.id)

    context = {
        "favorites": favorites
    }

    return render(request, 'cart/favorites.html', context)


def add_to_cart(request):
    product_id = request.POST.get('product')
    product = Product.objects.get(id=product_id)
    product_quantity = request.POST.get('cart_quantity')

    cart = Cart.objects.create(
        user=request.user,
        product=product,
        total_price=product.price * int(product_quantity),
        total_quantity=product_quantity
    )
    
    cart.save()
    messages.success(request, "Added to cart!")

    return redirect('product_detail', product_id)


def cart_list(request):
    user = request.user

    cart = Cart.objects.filter(user=user.id)

    final_price = 0
    for product in cart:
        final_price += product.total_price

    product_count = len(cart)

    context = {
        "cart": cart,
        "final_price": final_price,
        "product_count": product_count
    }
    return render(request, 'cart/cart.html', context)


def remove_cart(request, pk):
    Cart.objects.get(id=pk).delete()
    messages.success(request, 'Product removed!')

    return redirect('cart_list')


def remove_all_cart(request):
    user_id = request.user.id
    carts = Cart.objects.filter(user=user_id)

    for cart in carts:
        cart.delete()

    messages.success(request, "Remove all!")
    return redirect('cart_list')
