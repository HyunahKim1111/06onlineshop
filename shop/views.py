from django.shortcuts import render, get_object_or_404 # 해당 모델의 특정 object가 있으면 띄워주고 없으면 404페이지 띄워줌

from .models import *
from cart.forms import AddProductForm

def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True) # 제품을 보여줄 수 있는 애들만 보여주겠다.
    if category_slug:
        current_category = get_object_or_404(Category,slug=category_slug) # 카테고리 모델에서 슬러그가 category_slug인 애를 불러올거야.
        products = products.filter(category=current_category) # products에서 filter를 해서 category가 current_category인 애들을 불러올거야
    return render(request, 'shop/list.html', 
                  {
                      'current_category':current_category,
                      'categories':categories,
                      'products':products,
                      }) # 변수 넣어주면 원하는 데이터를 전부 템플릿으로 넘겨줄 수 있고, 템플릿에서 변수들을 가지고 디스플레이를 하면 돼.

def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity':1})
    return render(request, 'shop/detail.html', {'product':product, 'add_to_cart':add_to_cart})
