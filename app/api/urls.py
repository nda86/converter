from django.urls import path, re_path
from .views import Update, Rate, ListCurrencies


# список урл записей
urlpatterns = [
    path("update", Update.as_view()),
    path("currencies", ListCurrencies.as_view()),
    re_path(r"rate/(?P<cur_id>\d{0,3})", Rate.as_view())
]