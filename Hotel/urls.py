from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.HotelCreateView.as_view(), name="hotel_create"),
    path("", views.HotelListView.as_view(), name="hotel_list"),
    path("<slug:slug>/", views.HotelDetailView.as_view(), name="hotel_detail"),
    path("<slug:slug>/update/", views.HotelUpdateView.as_view(), name="hotel_update"),
    path("<slug:slug>/delete/", views.HotelDeleteView.as_view(), name="hotel_delete"),
]