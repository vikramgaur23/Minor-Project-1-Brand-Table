"""cafet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:table_num>/',views.home),
    path('register',views.signupView,name="signup"),
    path('login',views.signinView,name="signin"),
    path('cart',include('cart.urls')),
    path('main',views.main),
    path('order/', include('order.urls')),
    path('table/',include('Table.urls')),
 ]
