from django.contrib import admin
from .models import Category, Brand, Clothes


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_slug', 'category_description')
    list_display_links = ('id', 'category_name')
    prepopulated_fields = {'category_slug': ('category_name',)}
    search_fields = ('category_name', 'category_description')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_name', 'brand_slug', 'brand_description')
    list_display_links = ('id', 'brand_name')
    prepopulated_fields = {'brand_slug': ('brand_name',)}
    search_fields = ('brand_name', 'brand_description')


class ClothesAdmin(admin.ModelAdmin):
    list_display = ('id', 'clothes_name', 'owner', 'clothes_description', 'clothes_slug', 'clothes_type', 'clothes_season', 'clothes_price', 'clothes_image', )
    list_display_links = ('id', 'clothes_name')
    prepopulated_fields = {'clothes_slug': ('clothes_name',)}
    search_fields = ('clothes_name', 'clothes_description',  'clothes_brand__brand_name', 'clothes_category__category_name', )
    list_filter = ('clothes_type', 'clothes_season', 'clothes_brand', 'clothes_category', )
    list_select_related = ('clothes_brand', 'clothes_category', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Clothes, ClothesAdmin)
