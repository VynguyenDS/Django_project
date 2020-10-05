from django.urls import path
from . import views
urlpatterns = [
    path('',views.mainpage),
    path('table_page',views.table_page, name = 'table'),
    path('product_details',views.product_details, name = 'product_details'),
    path("insertProducts", views.insert_products, name="insertProducts"),
]