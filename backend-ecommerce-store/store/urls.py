from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('api/v1/', views.ProductListView.as_view(), name='store_home'),
    path('api/v1/<slug:slug>/', views.Product.as_view(), name='product'),
    path('api/v1/category/<slug:slug>/', views.CategoryItemView.as_view(), name='category_item'),
]
