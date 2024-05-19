from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from cart.models import Favorite, Cart
from .models import Product, Category
from .service import send_message


def index(request):
    products = list(Product.objects.all())

    if len(products) >= 3:
        products = products[:3:]

    context = {
        "products": products
    }
    return render(request, 'shop/index.html', context)


def listing(request, pk=None):
    categories = Category.objects.all()
    products = Product.objects.all()

    if pk:
        products = Product.objects.filter(Category_id=int(pk))

    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        "categories": categories,
        "products": products
    }

    return render(request, 'shop/listing.html', context)


def product_detail(request, pk):
    user = None if str(request.user) == 'AnonymousUser' else request.user.id
    favorites = Favorite.objects.filter(user=user)
    favorites = [str(i) for i in favorites]

    product = get_object_or_404(Product, id=pk)

    context = {
        "product": product,
        "favorites": favorites
    }

    return render(request, 'shop/product_detail.html', context)


def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')

        products = list(Product.objects.filter(name__contains=searched))

        category = Category.objects.filter(name__contains=searched)
        l = []
        for cat in category:
            _products = list(Product.objects.filter(Category_id=cat.id))
            l.append(_products)

        if products:
            products += l[0]

        context = {
            "products": products,
            "searched": searched
        }

        return render(request, 'shop/search.html', context)


def send_message_to_bot(request):
    if request.method == 'POST':
        user = request.user
        cart = Cart.objects.filter(user=user.id)
        card_number = request.POST.get('card_number')
        card_holder = request.POST.get('username')

        product_str = ""
        final_price = 0
        for product in cart:
            final_price += product.total_price
            product_str += (f"\n\tProduct name: {product.product.name}"
                            f"\n\tCount: {product.total_quantity}"
                            f"\n\tPrice: {product.total_price} som\n")
        message = f"""
        ORDER FROM SITE*
        Email: {user.email}
        Card holder: {card_holder}
        Card number: {card_number}
        Products: {product_str}
        ______________________
        Total price: {final_price} som
        """

        send_message(message)
        messages.success(request, "Order make success!")
        return redirect('home')
    return redirect('home')
