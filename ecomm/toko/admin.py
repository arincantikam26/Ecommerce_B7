from django.contrib import admin
from .models import ProdukItem, OrderProdukItem, Order, AlamatPengiriman, Payment, ProdukImage, Article

class ProdukItemAdmin(admin.ModelAdmin):
    list_display = ['nama_produk','harga', 'harga_diskon', 'slug',
                    'deskripsi', 'gambar', 'label', 'rating', 'kategori']

class ProdukImageAdmin(admin.ModelAdmin):
    list_display = ['produk', 'gambar']

class OrderProdukItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'produk_item', 'quantity']

class ArticleItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'tanggal_mulai', 'tanggal_order', 'ordered']

class AlamatPengirimanAdmin(admin.ModelAdmin):
    list_display = ['user', 'alamat_1', 'alamat_2', 'kode_pos', 'negara']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'timestamp', 'payment_option', 'charge_id']

admin.site.register(ProdukItem, ProdukItemAdmin)
admin.site.register(ProdukImage, ProdukImageAdmin)
admin.site.register(OrderProdukItem, OrderProdukItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(AlamatPengiriman, AlamatPengirimanAdmin)
admin.site.register(Payment, PaymentAdmin)
