from django.urls import path

from . import views


urlpatterns = [
    path("async/", views.async_view),
    path("sync/", views.sync_view),
    path('', views.index, name='home'),
]

