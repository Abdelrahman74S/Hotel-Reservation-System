from django.urls import path
from . import views

urlpatterns = [
    # Hotels
    path("", views.HotelListView.as_view(), name="hotel_list"),
    path("create/", views.HotelCreateView.as_view(), name="hotel_create"),
    path("<slug:slug>/", views.HotelDetailView.as_view(), name="hotel_detail"),
    path("<slug:slug>/update/", views.HotelUpdateView.as_view(), name="hotel_update"),
    path("<slug:slug>/delete/", views.HotelDeleteView.as_view(), name="hotel_delete"),

    # Room Categories
    path("categories/", views.RoomCategoryListView.as_view(), name="room_category_list"),
    path("categories/create/", views.RoomCategoryCreateView.as_view(), name="room_category_create"),
    path("categories/<int:pk>/", views.RoomCategoryDetailView.as_view(), name="room_category_detail"),
    path("categories/<int:pk>/update/", views.RoomCategoryUpdateView.as_view(), name="room_category_update"),
    path("categories/<int:pk>/delete/", views.RoomCategoryDeleteView.as_view(), name="room_category_delete"),

    # Rooms
    path("rooms/", views.RoomListView.as_view(), name="room_list"),
    path("rooms/create/", views.RoomCreateView.as_view(), name="room_create"),
    path("rooms/<int:pk>/", views.RoomDetailView.as_view(), name="room_detail"),
    path("rooms/<int:pk>/update/", views.RoomUpdateView.as_view(), name="room_update"),
    path("rooms/<int:pk>/delete/", views.RoomDeleteView.as_view(), name="room_delete"),

    # Hotel Images
    path("images/", views.HotelImageListView.as_view(), name="hotel_image_list"),
    path("images/create/", views.HotelImageCreateView.as_view(), name="hotel_image_create"),
    path("images/<int:pk>/update/", views.HotelImageUpdateView.as_view(), name="hotel_image_update"),
    path("images/<int:pk>/delete/", views.HotelImageDeleteView.as_view(), name="hotel_image_delete"),

    # Room Features
    path("features/", views.RoomFeatureListView.as_view(), name="room_feature_list"),
    path("features/create/", views.RoomFeatureCreateView.as_view(), name="room_feature_create"),
    path("features/<int:pk>/", views.RoomFeatureDetailView.as_view(), name="room_feature_detail"),
    path("features/<int:pk>/update/", views.RoomFeatureUpdateView.as_view(), name="room_feature_update"),
    path("features/<int:pk>/delete/", views.RoomFeatureDeleteView.as_view(), name="room_feature_delete"),
]
