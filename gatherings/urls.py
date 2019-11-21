from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllGatherings.as_view(), name='gatherings'),
    path('add/', views.GatheringCreate.as_view(), name='gathering-add'),
    path('<int:pk>', views.GatheringUpdate.as_view(), name='gathering-update'),
    path('<int:pk>/delete/', views.GatheringDelete.as_view(), name='gathering-delete')
]
