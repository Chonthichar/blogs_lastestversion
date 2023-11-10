from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from . import views
from .views import user_logout, Home, Detaisl_View, EditPostView, DeletePostView, LikeView, AddCommentpage

app_name = 'blog'

urlpatterns = [
    # path('', views.post, name='post'),
    # path('create/', views.create_post, name='create_pots'),
    # path('<int:primary_key>/edit/', views.post_edit, name='post_edit'),
    # path('<int:primary_key>/delete/', views.post_delete, name='post_delete'),
    path('', views.home, name='home'),
    path('art/<int:title_id>', views.detail, name='detail'),  # add pots
    path('add_fields/', views.fill_in_form, name='add_fields'),  # add pots
    # path('add_fields/', AddPost.as_view(), name='add_fields'), # add pots

    path('<int:title_id>/<str:author_name>/', views.user_blog, name='user_blog'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),  # This included log in and log out views by default
    # path('logout/', views.user_logout, name='logout')
    path('logout/', LogoutView.as_view(), name='logout'),
    path('post/', Home.as_view(), name='home_class'),  # Test Delete later
    path('article/<int:pk>', Detaisl_View.as_view(), name='article'),  # Test Delete later
    path('<int:pk>/edit', EditPostView.as_view(), name='edit_post'),  # Edit
    path('delete/<int:pk>', DeletePostView.as_view(), name='delete_blog'),
    path('like/<int:pk>', LikeView, name='like_post'),
    # path('article/<int:pk>/comment/', AddCommentpage.as_view(), name='post_comment'),
    path('article/<int:pk>/comment/', AddCommentpage.as_view(), name='post_comment'),

    # movie/1
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
