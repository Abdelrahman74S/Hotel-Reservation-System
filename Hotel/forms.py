from django import forms
from .models import Hotel, HotelImage, RoomFeature, RoomCategory, Room


class TailwindFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 bg-white"
                }
            )


class HotelForm(TailwindFormMixin, forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ["name", "slug", "address", "description", "website"]
        widgets = {
            "address": forms.Textarea(
                attrs={"rows": 2, "placeholder": "Enter full hotel address..."}
            ),
            "description": forms.Textarea(
                attrs={"rows": 4, "placeholder": "Describe your hotel..."}
            ),
        }


class HotelImageForm(TailwindFormMixin, forms.ModelForm):
    class Meta:
        model = HotelImage
        fields = ["hotel", "image", "is_primary"]
        help_texts = {"is_primary": "Check this if it is the main cover photo."}


class RoomFeatureForm(TailwindFormMixin, forms.ModelForm):
    class Meta:
        model = RoomFeature
        fields = ["name", "icon"]


class RoomCategoryForm(TailwindFormMixin, forms.ModelForm):
    class Meta:
        model = RoomCategory
        fields = [
            "hotel",
            "title",
            "base_price",
            "capacity_adults",
            "capacity_child",
            "description",
            "features",
        ]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "features": forms.CheckboxSelectMultiple(),
        }


class RoomForm(TailwindFormMixin, forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            "category",
            "room_number",
            "room_type",
            "price_override",
            "is_available",
        ]
        help_texts = {
            "price_override": "Optional: Set a specific price for this room only."
        }
