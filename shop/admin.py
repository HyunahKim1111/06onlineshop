from django.contrib import admin
from .models import *

# 첫번째 방법
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':['name']}

admin.site.register(Category, CategoryAdmin)

#첫 번째 방법 설명
# 카테고리 모델을 관리자페이지에서 보여줄 것입니다. 목록에 대한 옵션을 조절하고싶으면 만들어놓은 CategoryAdmin을 연결하면 된다.
# prepopulated_fields 는 카테고리를 등록할 때 뭐랑,뭐랑 섞어서 필드를 만들어주겠다.

# 두 번째 방법
@admin.register(Product) # 모델명을 써줘야 해.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug', 'category', 'price', 'stock', 'available_display', 'available_order', 'created', 'updated']
    list_filter = ['available_display', 'available_order', 'created', 'updated', 'category']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price', 'stock', 'available_display', 'available_order']

#두 번째 방법 설명
# 어노테이션 기법(데코레이터): @admin.register(Product) 이거를 class를 부르기 전에 적용하겠다. 보통 어노테이션은 함수에서 많이 쓴다. 근데 옵션 부분에서도 어노테이션을 쓴다.