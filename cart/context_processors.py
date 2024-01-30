from cart.apps import CartConfig
from main.models import Book


def cart_total_price(request):
    cart = request.session.get(CartConfig.cart_session_key, {})

    items = list(map(lambda x: {'book': x[0],
                                'count': x[1],
                                'total_price': x[0].get_price() * x[1],
                                'total_discount': x[0].price * x[1]},
                     [(Book.objects.get(id=int(id)), int(count)) for id, count in cart.items()]))

    total_price = sum([item.get('total_price') for item in items], 0)

    return {'cart': {
        'total_price': total_price,
        'items': items,
        'book_count': sum([item['count'] for item in items])
    }}
