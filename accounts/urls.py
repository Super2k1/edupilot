from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>', views.account_list_view),
]
