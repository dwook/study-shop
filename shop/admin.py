from django.contrib import admin

from .models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}  # slug 필드는 name 필드의 값에 따라 자동으로 설정. 어드민에서 카테고리 등록 시 Name 입력하면 Slug도 자동입력.

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','category','price','stock','available_display','available_order','created','updated']
    list_filter = ['available_display','created','updated','category']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price','stock','available_display','available_order']

admin.site.register(Product, ProductAdmin)
