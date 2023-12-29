from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST # 함수형 뷰에 데코레이션을 해주는 기능

from shop.models import Product
from .forms import AddProductForm
from .cart import Cart

@require_POST
def add(request, product_id): # request를 제외한 뒤에 나오는 매개변수들은 주소에 저 내용이 포함되게 넘길거구나.
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    #클라이언트 -> 서버로 데이터를 전달  
    # 유효성 검사, injection 처리
    form = AddProductForm(request.POST) 

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],is_update=cd['is_update'])

    return redirect('cart:detail')

def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)# 제품이 있으면 나오고 없으면 404페이지 띄워.
    cart.remove(product)
    return redirect('cart:detail')

def detail(request):
    cart = Cart(request)
    for product in cart:
        product['quantity_form'] = AddProductForm(initial={'quantity':product['quantity'], 'is_update':True})
        
    return render(request, 'cart/detail.html', {'cart':cart})