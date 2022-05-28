from django.db import models

class Vehicle(models.Model):
    vehicle_id = models.IntegerField(null=False, unique=True, primary_key=True)
    city = models.ForeignKey("City", on_delete=models.CASCADE)
    fuel_consumption = models.PositiveIntegerField(null=False, blank=False)
    distance_traveled = models.BigIntegerField(default=0)
    fuel_consumed = models.BigIntegerField(default=0)

    def __str__(self):
        txt = f"Vehicle: {self.vehicle_id}"
        return txt

    class Meta:
        db_table = 'Vehicle'
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'
        ordering =['vehicle_id']


class City(models.Model):
    city = models.CharField(max_length=100, null=False, blank=False, unique=True)

    def __str__(self):
        txt = f"{self.city}"
        return txt

    class Meta:
        db_table = 'City'
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'


class Event(models.Model):
    vehicle = models.ForeignKey("Vehicle", on_delete=models.CASCADE)
    new_city = models.ForeignKey("City", on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Event'
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering =['date_created']
        
class Route(models.Model):
    route_id = models.IntegerField(null=False, unique=True, primary_key=True) 
    distance = models.PositiveIntegerField(default=0)
    
    class Meta:
        db_table = 'Route'
        verbose_name = 'ruta'
        verbose_name_plural = 'rutas'
