from django.urls import path


from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catagorys/', views.CatagoryListView.as_view(), name='catagorys'),
    path('catagory/<int:pk>', views.CatagoryDetailView.as_view(), name = 'catagory_detail'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
    path('customers/', views.CustomerListView.as_view(), name='customers'),
    path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('orders', views.OrderListView.as_view(), name='orders'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('catagory/create', views.CatagoryCreate, name='catagory_create'),
    path('catagory/<int:pk>/update', views.CatagoryUpdate, name='catagory_update'),
    path('catagory/<int:pk>/delete', views.CatagoryDelete, name='catagory_delete'),
    path('product/create', views.ProductCreate, name='product_create'),
    path('product/<int:pk>/update', views.ProductUpdate, name='product_update'),
    path('product/<int:pk>/delete', views.ProductDelete, name='product_delete'),
    path('customer/create', views.CustomerCreate, name='customer_create'),
    path('customer/<int:pk>/update', views.CustomerUpdate, name='customer_update'),
    path('customer/<int:pk>/delete', views.CustomerDelete, name='customer_delete'),
    path('order/create', views.OrderCreate, name='order_create'),
    path('order/<int:pk>/update', views.OrderUpdate, name='order_update'),
    path('order/<int:pk>/delete', views.OrderDelete, name='order_delete'),
    path('upload/', views.upload_file, name='upload_file')

]

