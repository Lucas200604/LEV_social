from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index ,name='home'),
    path('about/', views.about),
    path('signup/', views.register, name='signup'),
    path('feed/', views.customfeed, name='feed'),
    path('logout/', views.signout, name='logout'),
    path('accounts/logout/', views.signout),
    path('login/', views.signin, name='login'),
    path('post/', views.post, name='post'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    path('edit-profile/', views.update_profile, name='edit-profile'),
    path('like/<int:pk>', views.LikeView, name='like_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)