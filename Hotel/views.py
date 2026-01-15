from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel, HotelImage, RoomFeature, RoomCategory, Room
from .forms import HotelForm, HotelImageForm, RoomFeatureForm, RoomCategoryForm, RoomForm
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .Permissions import ManagerRequiredMixin

# View for Hotel
class HotelCreateView(LoginRequiredMixin,ManagerRequiredMixin, CreateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'hotel/hotel_form.html'
    success_url = reverse_lazy('hotel_list')
    
class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel/hotel_list.html'
    context_object_name = 'hotels'
    
    def get_queryset(self):
        return Hotel.objects.all().prefetch_related('images')

class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'hotel/hotel_detail.html'
    context_object_name = 'hotel'
    slug_url_kwarg = 'slug' 
    
    def get_queryset(self):
        return Hotel.objects.all().prefetch_related(
            'images', 
            'categories__features', 
            'categories__rooms'
        )
    
class HotelUpdateView(LoginRequiredMixin,ManagerRequiredMixin, UpdateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'hotel/hotel_form.html'
    success_url = reverse_lazy('hotel_list')
    
@login_required
def hotel_delete_view(request, pk):
    if not request.user.is_authenticated or request.user.user_type != 'M':
        return redirect('login')
        
    hotel = get_object_or_404(Hotel, pk=pk)
    if request.method == 'POST':
        hotel.delete()
        return redirect('hotel_list')
    return render(request, 'hotel/hotel_confirm_delete.html', {'hotel': hotel})


# View for RoomCategory 
class RoomCategoryCreateView(LoginRequiredMixin,ManagerRequiredMixin, CreateView):
    model = RoomCategory
    form_class = RoomCategoryForm
    template_name = 'hotel/roomcategory_form.html'
    success_url = reverse_lazy('hotel_list')
    
class RoomCategoryListView(ListView):
    model = RoomCategory
    template_name = 'hotel/roomcategory_list.html'
    context_object_name = 'room_categories'
    
    def get_queryset(self):
        return RoomCategory.objects.all.select_related('hotel').prefetch_related('features', 'rooms')
    
class RoomCategoryDetailView(DetailView):
    model = RoomCategory
    template_name = 'hotel/roomcategory_detail.html'
    context_object_name = 'room_category'
    
    def get_queryset(self):
        return RoomCategory.objects.all().select_related('hotel').prefetch_related('features', 'rooms')
    
class RoomCategoryUpdateView(LoginRequiredMixin,ManagerRequiredMixin, UpdateView):
    model = RoomCategory
    form_class = RoomCategoryForm
    template_name = 'hotel/roomcategory_form.html'
    success_url = reverse_lazy('hotel_list')
    
@login_required
def roomcategory_delete_view(request, pk):
    if not request.user.is_authenticated or request.user.user_type != 'M':
        return redirect('login')
        
    room_category = get_object_or_404(RoomCategory, pk=pk)
    if request.method == 'POST':
        room_category.delete()
        return redirect('hotel_list')
    return render(request, 'hotel/roomcategory_confirm_delete.html', {'room_category': room_category})

# views for HotelImage , and Room can be implemented similarly.
class HotelImageCreateView(LoginRequiredMixin,ManagerRequiredMixin, CreateView):
    model = HotelImage
    form_class = HotelImageForm
    template_name = 'hotel/hotel_image_form.html'
    success_url = reverse_lazy('hotel_list')

class HotelImageListView(ListView):
    model = HotelImage
    template_name = 'hotel/hotel_image_list.html'
    context_object_name = 'hotel_images'

    def get_queryset(self):
        return HotelImage.objects.all().select_related('hotel')
    
class HotelImageDetailView(DetailView):
    model = HotelImage
    template_name = 'hotel/hotel_image_detail.html'
    context_object_name = 'hotel_image'
    
    def get_queryset(self):
        return HotelImage.objects.all().select_related('hotel')

class HotelImageUpdateView(LoginRequiredMixin,ManagerRequiredMixin, UpdateView):
    model = HotelImage
    form_class = HotelImageForm
    template_name = 'hotel/hotel_image_form.html'
    success_url = reverse_lazy('hotel_list')
    
@login_required
def hotel_image_delete_view(request, pk):
    if not request.user.is_authenticated or request.user.user_type != 'M':
        return redirect('login')
        
    hotel_image = get_object_or_404(HotelImage, pk=pk)
    if request.method == 'POST':
        hotel_image.delete()
        return redirect('hotel_list')
    return render(request, 'hotel/hotel_image_confirm_delete.html', {'hotel_image': hotel_image})

# views for RoomFeature
class RoomFeatureCreateView(LoginRequiredMixin,ManagerRequiredMixin, CreateView):
    model = RoomFeature
    form_class = RoomFeatureForm
    template_name = 'hotel/room_feature_form.html'
    success_url = reverse_lazy('hotel_list')

class RoomFeatureListView(ListView):
    model = RoomFeature
    template_name = 'hotel/room_feature_list.html'
    context_object_name = 'room_features'

    def get_queryset(self):
        return RoomFeature.objects.all()   
    
class RoomFeatureDetailView(DetailView):
    model = RoomFeature
    template_name = 'hotel/room_feature_detail.html'
    context_object_name = 'room_feature'
    
    def get_queryset(self):
        return RoomFeature.objects.all()

class RoomFeatureUpdateView(LoginRequiredMixin,ManagerRequiredMixin, UpdateView):
    model = RoomFeature
    form_class = RoomFeatureForm
    template_name = 'hotel/room_feature_form.html'
    success_url = reverse_lazy('hotel_list')

@login_required
def room_feature_delete_view(request, pk):
    if not request.user.is_authenticated or request.user.user_type != 'M':
        return redirect('login')  
    room_feature = get_object_or_404(RoomFeature, pk=pk)
    if request.method == 'POST':
        room_feature.delete()
        return redirect('hotel_list')
    return render(request, 'hotel/room_feature_confirm_delete.html', {'room_feature': room_feature})

# views for Room
class RoomCreateView(LoginRequiredMixin,ManagerRequiredMixin, CreateView):
    model = Room
    form_class = RoomForm
    template_name = 'hotel/room_form.html'
    success_url = reverse_lazy('hotel_list')
    
class RoomListView(ListView):
    model = Room
    template_name = 'hotel/room_list.html'
    context_object_name = 'rooms'
    
    def get_queryset(self):
        return Room.objects.all().select_related('category')

class RoomDetailView(DetailView):
    model = Room
    template_name = 'hotel/room_detail.html'
    context_object_name = 'room'
    
    def get_queryset(self):
        return Room.objects.all().select_related('category')    
    
class RoomUpdateView(LoginRequiredMixin,ManagerRequiredMixin, UpdateView):
    model = Room
    form_class = RoomForm
    template_name = 'hotel/room_form.html'
    success_url = reverse_lazy('hotel_list')
    
@login_required
def room_delete_view(request, pk):  
    if not request.user.is_authenticated or request.user.user_type != 'M':
        return redirect('login')
        
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('hotel_list')
    return render(request, 'hotel/room_confirm_delete.html', {'room': room})
