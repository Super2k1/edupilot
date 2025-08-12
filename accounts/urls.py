from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.account_create_view, name='account-create'),
    path('', views.account_list_view, name='account-list'),
    path('<int:pk>/', views.account_detail_view, name='account-detail'),  # Note the trailing slash
    path('<int:pk>/update/', views.account_update_view, name='account-update'),
    path('<int:pk>/delete/', views.account_delete_view, name='account-delete'),
]
