from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CustomUserCreationForm, PostForm, ProfileUpdateForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.urls import reverse



# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('hola')


def customfeed(request):
    posts = Post.objects.all()

    return render(request, 'feed.html', {
        'posts': posts
    })

# Register user
def register(request):

    if request.method == 'GET':
        print('enviando formulario')
        return render(request, 'registration/signup.html', {
            'form': CustomUserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.create_user(
                    username=request.POST['username'],email=request.POST['email'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('feed')

            except IntegrityError:
                return render(request, 'registration/signup.html', {
                    'form': CustomUserCreationForm(),
                    'error': '*Nombre de Usuario existente',
                })

        return render(request, 'registration/signup.html', {
            'form': CustomUserCreationForm(),
            'error': '*Las contraseñas no coinciden',
        })


def signout(request):
    logout(request)
    return redirect('home')



def signin(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'registration/login.html', {
            'form': AuthenticationForm,
            'error': 'El nombre de usuario o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('feed')
        
@login_required        
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'post.html', {'form':form})    

@login_required
def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'profile.html', {'user': user, 'posts':posts})

@login_required
def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    return redirect('profile')

@login_required
def unfollow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    return redirect('profile')


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'edit-profile.html', {'form': form})

@login_required
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return redirect('feed')