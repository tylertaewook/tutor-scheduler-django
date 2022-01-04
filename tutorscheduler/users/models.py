from django.db import models
from django.contrib.auth.models import Group, User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Teacher(models.Model):
    WEEKDAY_CHOICES = (
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wednesday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday"),
        ("SATURDAY", "Saturday"),
        ("SUNDAY", "Sunday"),
    )

    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=100)
    assigned_day = models.CharField(
        max_length=10, choices=WEEKDAY_CHOICES, default="MONDAY"
    )

    def __str__(self):
        return self.assigned_day

