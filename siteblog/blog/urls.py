from django.urls import path

from .views import IndexView
from .views import PostDetailView
from .views import PostByCategory
from .views import PostByTag
from .views import Search

app_name = 'blog'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<slug:slug>/', PostByCategory.as_view(), name='category'),
    path('tag/<slug:slug>/', PostByTag.as_view(), name='tag'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post'),
    path('search/', Search.as_view(), name='search')
]
