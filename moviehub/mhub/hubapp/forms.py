from django import forms
from django.contrib.auth.models import User

from .models import Movie, Category, Review, Profile


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name','rating', 'image', 'description', 'release_year', 'actors', 'category', 'youtube_trailer_link']
        widgets = {
            'release_year': forms.NumberInput(attrs={'min': 1900, 'max': 2100, 'placeholder': 'Enter Release Year'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'desc', 'img']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'profile_picture']

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)], label="Rating")

    class Meta:
        model = Review
        fields = ['comment', 'rating']


