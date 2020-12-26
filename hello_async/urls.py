from django.urls import path

from . import views


urlpatterns = [
    path('smoke_some_meats/', views.smoke_some_meats),
    path('smoke_some_meats2/', views.smoke_some_meats2),

    path('burn_some_meats/', views.burn_some_meats),
    path('sync_to_async/', views.async_with_sync_view),

    path('async/', views.async_view),
    path('sync/', views.sync_view),

    path('', views.index, name='home'),
]

