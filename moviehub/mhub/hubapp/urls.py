from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('account/', views.account, name='account'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('add_movie/',views.add_movie,name='add_movie'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('movie/edit/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('movie/delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('movie/<int:movie_id>/add-review/', views.add_review, name='add_review'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('search/', views.search, name='search'),
    path('category/<int:category_id>/',views.category, name='category'),
]


