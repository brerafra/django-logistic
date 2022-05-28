from django.shortcuts import render,get_object_or_404
from .models import Vehicle,Event,City,Route
from rest_framework import viewsets
from .serializers import VehicleSerializer,EventSerializer
from rest_framework.response import Response
from rest_framework import status

def index(request):
    return render(request,'index.html')

def cityView(request,city):
    if request.method=='GET':
        vehicles = Vehicle.objects.filter(city=city)
        print(vehicles)

        context = {
            'vehicles':vehicles,
        }

        return render(request,'city.html',context)
    else:
        return render(request,'index.html')


class VehicleViewset(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        vehicle = Vehicle.objects.get(vehicle_id=request.data['vehicle'])

        if vehicle.city.id == int(request.data['new_city']):
            return Response({'message':'Same city not allowed'},status=status.HTTP_404_NOT_FOUND)
        
        if vehicle.city.id == 1 and request.data['new_city']=='2' or vehicle.city.id == 2 and request.data['new_city']=='1':
            route = Route.objects.get(route_id=1)
            distance = route.distance
        elif vehicle.city.id == 2 and request.data['new_city']=='3' or vehicle.city.id == 3 and request.data['new_city']=='2':
            route = Route.objects.get(route_id=2)
            distance = route.distance
        elif vehicle.city.id == 3 and request.data['new_city']=='1' or vehicle.city.id == 1 and request.data['new_city']=='3':
            route = Route.objects.get(route_id=2)
            distance = route.distance
        else:
            distance = 0
            
            
        total_distance = vehicle.distance_traveled + distance
        fuel_consumed = vehicle.fuel_consumed + distance*vehicle.fuel_consumption

        defaults={'city': City.objects.get(id=request.data['new_city']),'distance_traveled':total_distance, 'fuel_consumed':fuel_consumed}

        Vehicle.objects.update_or_create(vehicle_id=vehicle.vehicle_id,defaults=defaults)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    def retrieve(self, request, pk=None):
        return Response({'message':'not allowed'})

    def update(self, request, pk=None):
        return Response({'message':'not allowed'})

    def partial_update(self, request, pk=None):
        return Response({'message':'not allowed'})

    def destroy(self, request, pk=None):
        return Response({'message':'not allowed'})

    def perform_create(self, serializer):
        serializer.save()
