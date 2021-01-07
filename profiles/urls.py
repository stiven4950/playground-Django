from django.urls import path

from .views import ProfileListView, ProfileDetailView

profiles_patterns = ([
    path('list/', ProfileListView.as_view(), name='list'),
    path('<username>/', ProfileDetailView.as_view(), name='detail'),
], "profiles")