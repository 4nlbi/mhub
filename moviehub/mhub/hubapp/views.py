from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm, ReviewForm, UserForm, ProfileForm, CategoryForm
from .models import Movie, Category, Profile


# Create your views here.
def index(request):
    categories = Category.objects.all()  # Fetch all categories
    movies = Movie.objects.all()  # Fetch all movies

    context = {
        'categories': categories,
        'movies': movies,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def account(request):
    if request.method== 'POST':
        username=request.POST['username']
        Fname= request.POST['first_name']
        Lname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['conform_password']

        if password== cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('account')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is taken")
                return redirect('account')
            user=User.objects.create_user(username=username,first_name=Fname,last_name=Lname,email=email,password=password)
            user.save();
            return redirect('login')
            print('user created')
        else:
            messages.info(request,"passwoard not match")
            return redirect('account')
        return redirect('/')

    return render(request,"account.html")



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid password")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def add_movie(request):
    if not request.user.is_authenticated:
        return redirect('/login/')  # Redirect to the login page

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user  # Set the user who added the movie
            movie.save()
            messages.success(request, 'Movie added successfully!')
            return redirect('/')  # Redirect to your home page or movie list page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MovieForm()

    return render(request, 'add_movie.html', {'form': form})



def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id, added_by=request.user)  # Ensure movie belongs to user
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie updated successfully!')
            return redirect('profile')  # Redirect to profile page or movie list
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = MovieForm(instance=movie)

    return render(request, 'edit.html', {'form': form})


def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    print(vars(movie))  # This will show all attributes of the movie object

    if request.method == 'POST':
        movie.delete()
        messages.success(request, f'The movie "{movie.title}" has been deleted successfully.')
        return redirect('profile')

    return render(request, 'delete.html', {'movie': movie})

def profile_view(request):
    return render(request, 'profile_view.html', {'user': request.user})



def edit_profile(request):
    if not hasattr(request.user, 'profile'):
        Profile.objects.create(user=request.user)  # Create a profile if it does not exist

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile_view')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})



def add_review(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user  # assumes user is logged in
            review.save()
            return redirect('index')  # Correct the redirect
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'movie': movie, 'form': form})  # Ensure movie and form are passed here

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie_detail.html', {'movie': movie})


def movie_list(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 8)  # Show 8 movies per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'movie_list.html', {'page_obj': page_obj})

def search(request):
    query = request.GET.get('q', '')
    movie = Movie.objects.filter(name__icontains=query)  # Search by movie name

    # Check if the query matches any category name
    category = Category.objects.filter(name__iexact=query).first()
    if category:
        movie = Movie.objects.filter(category=category)  # Get all movies in that category

    return render(request, 'search.html', {'query': query, 'movie': movie})


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # Get the category by ID
    movies = Movie.objects.filter(category=category)  # Get movies related to the category
    return render(request, 'category.html', {'category': category, 'movies': movies})