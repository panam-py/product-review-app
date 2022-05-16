from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Product, ProductSize, ProductSite, Comment, Company, Category, Image

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'content',)
    list_filter = ('category',)


# admin.site.register(Product)
admin.site.register(ProductSize)
admin.site.register(ProductSite)
admin.site.register(Company)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Image)

admin.site.unregister(Group)

admin.site.site_header = "Product Review Admin"