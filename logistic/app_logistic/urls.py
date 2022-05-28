from django.urls import path,include
from rest_framework import routers
from . import views
from .views import VehicleViewset, EventViewset

router = routers.DefaultRouter()
router.register('vehicle', VehicleViewset)
router.register('event', EventViewset)

urlpatterns = [
    path('',views.index, name='index'),
    path('api/',include(router.urls)),
    path('city/<str:city>/', views.cityView, name='city'),
]