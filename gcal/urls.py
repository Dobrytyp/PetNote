from django.urls import path

from . import views

app_name = 'gcal'

urlpatterns = [
    path('event-list', views.EventList.as_view(), name='event-list'),
    path('event-detail/<int:pk>', views.EventDetail.as_view(), name='event-detail'),
    path('event-create', views.EventCreate.as_view(), name='event-create'),
    path('event-update/<int:pk>', views.EventUpdate.as_view(), name='event-update'),
    path('event-delete/<int:pk>', views.EventDelete.as_view(), name='event-delete'),
]
