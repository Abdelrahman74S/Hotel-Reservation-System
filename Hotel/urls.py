from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.HotelCreateView.as_view(), name='hotel_create'),
    path('list/', views.HotelListView.as_view(), name='hotel_list'), 
    path('<slug:slug>/', views.HotelDetailView.as_view(), name='hotel_detail'),
    path('<slug:slug>/update/', views.HotelUpdateView.as_view(), name='hotel_update'),
    path('<uuid:pk>/delete/', views.hotel_delete_view, name='hotel_delete'),
    path('roomcategory/create/', views.RoomCategoryCreateView.as_view(), name='roomcategory_create'),
    path('roomcategory/list/', views.RoomCategoryListView.as_view(), name='roomcategory_list'),
    path('roomcategory/<int:pk>/', views.RoomCategoryDetailView.as_view(), name='roomcategory_detail'),
    path('roomcategory/<int:pk>/update/', views.RoomCategoryUpdateView.as_view(), name='roomcategory_update'),
    path('roomcategory/<int:pk>/delete/', views.roomcategory_delete_view, name='roomcategory_delete'),
    path('hotel_image/create/', views.HotelImageCreateView.as_view(), name='hotel_image_create'),
    path('hotel_image/list/', views.HotelImageListView.as_view(), name='hotel_image_list'),
    path('hotel_image/<int:pk>/update/', views.HotelImageUpdateView.as_view(), name='hotel_image_update'),
    path('hotel_image/<int:pk>/delete/', views.hotelimage_delete_view, name='hotel_image_delete'),  
    path('roomfeature/create/', views.RoomFeatureCreateView.as_view(), name='roomfeature_create'),
    path('roomfeature/list/', views.RoomFeatureListView.as_view(), name='roomfeature_list'),
    path('roomfeature/<int:pk>/update/', views.RoomFeatureUpdateView.as_view(), name='roomfeature_update'),
    path('roomfeature/<int:pk>/delete/', views.roomfeature_delete_view, name='roomfeature_delete'),
    path('room/create/', views.RoomCreateView.as_view(), name='room_create'),
    path('room/list/', views.RoomListView.as_view(), name='room_list'),
    path('room/<uuid:pk>/', views.RoomDetailView.as_view(), name='room_detail'),
    path('room/<uuid:pk>/update/', views.RoomUpdateView.as_view(), name='room_update'),
    path('room/<uuid:pk>/delete/', views.room_delete_view, name='room_delete'),
    
]