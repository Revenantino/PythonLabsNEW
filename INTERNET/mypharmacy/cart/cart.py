from decimal import Decimal
from django.conf import settings
from pharmacy.models import Medicine


class Cart(object):
    def __init__(self, request):
        # Ініціалізація корзини користувача
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # зберігаємо корзину користувача в сесію
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    # добавлення товару в корзину користувача і обновлення кількості товару
    def add(self, medicine, quantity=1, update_quantity=False):
        medicine_id = str(medicine.id)
        if medicine_id not in self.cart:
            self.cart[medicine_id] = {
                'quantity': 0,
                'price': str(medicine.price)
            }
            if update_quantity:
                self.cart[medicine_id]['quantity'] = quantity
            else:
                self.cart[medicine_id]['quantity'] += quantity

    # зберігання даних в сксію
    def save(self):
        self.session[settings[CART_SESSION_ID]] = self.cart
        # вказуємо шо сессія змінена
        self.session.modified = True

    def remove(self, medicine):
        medicine_id = str(medicine.id)
        if medicine_id in self.cart:
            del self.cart[medicine_id]
            self.save()

    # ітерація по товарам
    def __iter__(self):
        medicine_ids = self.cart.keys()
        medicines = Medicine.objects.filter(id_in=medicine_ids)
        for medicine in medicines:
            self.cart[str(medicine.id)]['medicine'] = medicine

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    # кількість товару в корзині
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
