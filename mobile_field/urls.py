from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.products,name="products"),
    path('login/',views.login_system,name="login"),
    path('signup/',views.sign_up,name="signup"),
    path('checkotp/',views.checkotp,name="checkotp"),
]