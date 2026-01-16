from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import uuid

class Hotel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    address = models.TextField()
    description = models.TextField()
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def primary_image(self):
        return self.images.filter(is_primary=True).first()

    def get_absolute_url(self):
        return reverse("hotel_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="hotel_images/")
    is_primary = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.is_primary:
            HotelImage.objects.filter(hotel=self.hotel, is_primary=True).update(
                is_primary=False
            )
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-is_primary", "uploaded_at"]

    def __str__(self):
        return f"Image for {self.hotel.name}"


class RoomFeature(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(
        max_length=50, blank=True, null=True, help_text="FontAwesome icon class"
    )

    def __str__(self):
        return self.name


class RoomCategory(models.Model):
    hotel = models.ForeignKey(
        Hotel, related_name="categories", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity_adults = models.PositiveIntegerField()
    capacity_child = models.PositiveIntegerField()
    description = models.TextField()
    features = models.ManyToManyField(
        RoomFeature, related_name="categories", blank=True
    )

    def __str__(self):
        return f"{self.hotel.name} - {self.title}"


class Room(models.Model):
    ROOM_TYPES = [
        ("S", "Single"),
        ("D", "Double"),
        ("SU", "Suite"),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(
        RoomCategory, related_name="rooms", on_delete=models.CASCADE
    )
    room_number = models.CharField(max_length=10)
    room_type = models.CharField(max_length=2, choices=ROOM_TYPES)
    price_override = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    is_available = models.BooleanField(default=True)

    class Meta:
        unique_together = ("category", "room_number")

    def __str__(self):
        return f"{self.category.hotel.name} - Room {self.room_number}"
