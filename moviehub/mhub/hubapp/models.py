from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=20, unique=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='Category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

from django.conf import settings
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=250)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='movies')
    description = models.TextField()
    release_year = models.IntegerField()
    actors = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    youtube_trailer_link = models.URLField()
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    # Add any other fields you want

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Assuming you're using Django's auth
    comment = models.TextField()
    rating = models.PositiveIntegerField(default=1)  # 1-5 scale
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if not (1 <= self.rating <= 5):
            raise ValidationError('Rating must be between 1 and 5')


