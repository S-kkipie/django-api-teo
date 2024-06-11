from django.shortcuts import render

from rest_framework.response import Response
from .models import Plate
from .serializer import PlateSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def plate_list(request):
    plates = Plate.objects.all()
    serializer = PlateSerializer(plates, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def plate_detail(request, pk):
    plate = Plate.objects.get(id=pk)
    serializer = PlateSerializer(plate, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def plate_create(request):
    serializer = PlateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.data)


@api_view(['PUT'])
def plate_update(request, pk):
    plate = Plate.objects.get(id=pk)
    serializer = PlateSerializer(instance=plate, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def plate_delete(request, pk):
    plate = Plate.objects.get(id=pk)
    plate.delete()
    return Response('Plate deleted successfully')
