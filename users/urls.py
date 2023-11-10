from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from . import views
from .views import UserRegisterPageView, UserEditPageView, ProfilePageView, EditProfilePage, CreateProfilePageForUser
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('register/', UserRegisterPageView.as_view(), name='register'),
    path('edit_profile/', UserEditPageView.as_view(), name='edit_profile'),
    path('user/<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),
    path('user/<int:pk>/edit_profile_page/', EditProfilePage.as_view(), name='edit_profile_page'),
    path('create_profile/', CreateProfilePageForUser.as_view(), name='create_profile_page'),
# path('article/<int:pk>/comment/', AddCommentpage.as_view(), name='post_comment'),
        # path('<int:pk>/profile/', ProfilePageView.as_view(), name='show_profile_page')
    # path('users/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'), # overrid it becasue got an error import view
    # path('users/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # The problem before file need to be registration
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
