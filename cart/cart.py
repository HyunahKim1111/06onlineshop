from decimal import Decimal
from django.conf import settings

from shop.models import Product

class Cart(object):
    def __init__(self,request): # 초기화 작업
        self.session = request.session # 장고 뷰에서 사용했던 request가 들어있음.
        cart = self.session.get(settings.CART_ID)
        if not cart:
            cart = self.session[settings.CART_ID]
        self.cart = cart # 카트 객체의 현재 카트는 세션에서 불러 온 카트 혹은 새로 만든 카드야.라고 선언함.

    def __len__(self): # 이터레이터 등을 쓸 때 몇개 들어있는지 
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self): # for문 사용시 어떤 요소들을 건네줄건지
        product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=product_ids) # filter를 걸어서 원하는 애들만 가져올건데, id__in=product_ids 장바구니에 들어있는 애들만 주세요

        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']

            yield item

    def add(self, product, quantity=1, is_update=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity':0, 'price':str(product.price)}

        if is_update:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
    
        self.save()

    def save(self):
        self.session[settings.CART_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del(self.cart[product_id])
            self.save()

    def clear(self):
        self.session[settings.CART_ID] = {}
        self.session.modified = True

    def get_product_total(self):
        return sum(item['price']*item['quantity'] for item in self.cart.values())

