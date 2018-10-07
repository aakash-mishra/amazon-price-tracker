from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'', views.check_price, name="checkprice" )
]
