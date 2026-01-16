from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Hotel, RoomCategory, Room, HotelImage, RoomFeature, RoomCategory
from .forms import (
    HotelForm,
    RoomCategoryForm,
    HotelImageForm,
    RoomFeatureForm,
    RoomForm,
)
from .Permissions import ManagerRequiredMixin

class HotelCreateView(ManagerRequiredMixin, CreateView):
    model = Hotel
    form_class = HotelForm
    template_name = "hotel/hotel_form.html"
    success_url = reverse_lazy("hotel_list")


class HotelListView(ListView):
    model = Hotel
    template_name = "hotel/hotel_list.html"
    context_object_name = "hotels"

    def get_queryset(self):
        return Hotel.objects.all().prefetch_related("images")


class HotelDetailView(DetailView):
    model = Hotel
    template_name = "hotel/hotel_detail.html"
    context_object_name = "hotel"

    def get_queryset(self):
        return Hotel.objects.all().prefetch_related(
            "images", "categories__features", "categories__rooms"
        )


class HotelUpdateView(ManagerRequiredMixin, UpdateView):
    model = Hotel
    form_class = HotelForm
    template_name = "hotel/hotel_form.html"
    success_url = reverse_lazy("hotel_list")


class HotelDeleteView(ManagerRequiredMixin, DeleteView):
    model = Hotel
    template_name = "hotel/hotel_confirm_delete.html"
    success_url = reverse_lazy("hotel_list")


# (RoomCategory) 
class RoomCategoryListView(ListView):
    model = RoomCategory
    template_name = "hotel/room_category_list.html"
    context_object_name = "room_categories"

    def get_queryset(self):
        return RoomCategory.objects.all().select_related('hotel')

class RoomCategoryDetailView(DetailView):
    model = RoomCategory
    template_name = "hotel/roomcategory_detail.html"
    context_object_name = "room_category"

class RoomCategoryCreateView(ManagerRequiredMixin, CreateView):
    model = RoomCategory
    form_class = RoomCategoryForm
    template_name = "hotel/room_category_form.html"
    success_url = reverse_lazy("room_category_list")

class RoomCategoryUpdateView(ManagerRequiredMixin, UpdateView):
    model = RoomCategory
    form_class = RoomCategoryForm
    template_name = "hotel/room_category_form.html"
    success_url = reverse_lazy("room_category_list")

class RoomCategoryDeleteView(ManagerRequiredMixin, DeleteView):
    model = RoomCategory
    template_name = "hotel/roomcategory_confirm_delete.html"
    success_url = reverse_lazy("room_category_list")


# (Room) 
class RoomListView(ListView):
    model = Room
    template_name = "hotel/room_list.html"
    context_object_name = "rooms"

class RoomCreateView(ManagerRequiredMixin, CreateView):
    model = Room
    form_class = RoomForm
    template_name = "hotel/room_form.html"
    success_url = reverse_lazy("room_list")


# (HotelImage) 
class HotelImageListView(ListView):
    model = HotelImage
    template_name = "hotel/hotel_image_list.html"
    context_object_name = "hotel_images"

class HotelImageCreateView(ManagerRequiredMixin, CreateView):
    model = HotelImage
    form_class = HotelImageForm
    template_name = "hotel/hotel_image_form.html"
    success_url = reverse_lazy("hotel_image_list")


#  (RoomFeature)
class RoomFeatureListView(ListView):
    model = RoomFeature
    template_name = "hotel/room_feature_list.html"
    context_object_name = "room_features"

class RoomFeatureCreateView(ManagerRequiredMixin, CreateView):
    model = RoomFeature
    form_class = RoomFeatureForm
    template_name = "hotel/room_feature_form.html"
    success_url = reverse_lazy("room_feature_list")