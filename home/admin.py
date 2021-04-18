from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(Product,ProductAdmin)

class BirthdayAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(Birthday,BirthdayAdmin)

class CombosAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(Combos,CombosAdmin)

class SweetsAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(Sweets,SweetsAdmin)

class BeveregesAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(Bevereges,BeveregesAdmin)

class BurgerAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(Burger,BeveregesAdmin)

class ComboAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(Combo,ComboAdmin)

class ChineseAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(Chinese,ChineseAdmin)

class ParathaAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(Paratha,ParathaAdmin)

class IcecreamAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(Icecream,IcecreamAdmin)

class riceAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(rice,riceAdmin)

class rollsAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(rolls,rollsAdmin)

class sandwitchAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(sandwitch,sandwitchAdmin)

class SnacksAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(Snacks,SnacksAdmin)

class SouthIndianAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(SouthIndian,SouthIndianAdmin)

class ThaliAdmin(admin.ModelAdmin):
	list_display=['name','price','available']
	list_editable=['price','available']
	prepopulated_fields={'slug':('name',)}
	list_per_page=20
admin.site.register(Thali,ThaliAdmin)