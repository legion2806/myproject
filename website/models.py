from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # поле для аватара
    city = models.CharField(max_length=100, blank=True)  # город проживания
    hiking_experience = models.TextField(blank=True)  # описание опыта
    favorite_trail = models.CharField(max_length=255, blank=True)  # любимый маршрут
    future_goals = models.TextField(blank=True)  # цели на будущее
    equipment = models.TextField(blank=True)  # информация о снаряжении
    advice_for_beginners = models.TextField(blank=True)  # советы для новичков

    def __str__(self):
        return f"{self.user.username}'s Profile"