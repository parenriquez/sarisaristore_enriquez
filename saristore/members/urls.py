from django.urls import path
from members import views

urlpatterns = [
   path('home/', views.home, name = "home"),
   path('home/<int:product_id>/', views.product_detail, name='product_detail'),
   path('issue_item/<str:pk>/', views.issue_item, name='issue_item'),   
   path('update_stock/<str:pk>/', views.update_stock, name='update_stock'),
   path('delete_stock/<str:pk>',views.delete_stock, name='delete_stock'),
   path('add_new_stock/', views.add_new_stock, name='add_new_stock'),
   path('receipt/', views.receipt, name = "receipt"),
   path('receipt/<int:receipt_id>/', views.receipt_detail, name='receipt_detail'),
   path('all_sales/', views.all_sales, name = 'all_sales')
   
    ]

