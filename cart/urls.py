from django.urls import path
from django.conf.urls import url
from . import views

app_name='cart'

urlpatterns=[
	path('add/<int:product_id>/',views.add_cart,name='add_cart'),
	path('',views.cart_detail, name='cart_detail'),
	path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
	path('full_remove/<int:product_id>/',views.full_remove,name='full_remove'),
	path('history/' , views.orderHistory, name='order_history'),
	path('<int:order_id>/', views.viewOrder, name='order_detail'),
	
]