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
