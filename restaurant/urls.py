from django.urls import path
from django.contrib.auth.decorators import login_required

from .views  import IndexView, OrderView, DetailsView, login_user, logout_user

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('order/<int:pk>', login_required(OrderView.as_view()), name='order'),
    path('details/', login_required(DetailsView.as_view()), name='details'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
