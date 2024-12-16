from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:numeric_month>/", views.month_number_redirect),
    path("<str:month>/", views.monthly_challenge, name="monthly_challenge"),
]
