from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveAPIView, \
    ListAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination

from ..models import Property
from ..serializers import PropertySerializer, PropertyAvailibilitySerializer

# function-based view
@api_view(['GET'])
def test_message(request):
    return Response({"message":"hello it works!"})

class CreateProperty(CreateAPIView):
    serializer_class = PropertySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PropertyGetSet(RetrieveAPIView, UpdateAPIView):
    serializer_class = PropertySerializer
    def get_object(self):
        return get_object_or_404(Property, id=self.kwargs['pk'])

class PropertyList(ListAPIView):
    permission_classes = []
    serializer_class = PropertySerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        if self.request.method == 'GET':
            queryset = Property.objects.all()
            
            wifi = self.request.GET.get('wifi', None)
            if wifi is not None and wifi.lower() == 'true':
                    queryset = queryset.filter(wifi=True)

            petfriendly = self.request.GET.get('petfriendly', None)
            if petfriendly is not None and petfriendly.lower() == 'true':
                queryset = queryset.filter(petfriendly=True)

            tv = self.request.GET.get('tv', None)
            if tv is not None and tv.lower() == 'true':
                queryset = queryset.filter(tv=True)
            
            pillows = self.request.GET.get('pillows', None)
            if pillows is not None and pillows.lower() == 'true':
                queryset = queryset.filter(pillows=True)
            
            sortby = self.request.GET.get('sortby', None)
            if sortby is not None:
                if sortby.lower() == 'guests':
                    queryset = queryset.order_by('-number_of_guests')
                elif sortby.lower() == 'beds':
                    queryset = queryset.order_by('-number_of_beds')
            
            return queryset
        
class PropertyOwnedList(ListAPIView):
    serializer_class = PropertySerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        if self.request.method == 'GET':
            return self.request.user.property_set.all()
        
class PropertyDelete(DestroyAPIView):
    serializer_class = PropertySerializer
    
    def get_queryset(self):
        queryset = Property.objects.filter(id=self.kwargs['pk'], owner=self.request.user)
        return queryset

class PropertyAvailability(CreateAPIView):
    serializer_class = PropertyAvailibilitySerializer

    def create(self, request, *args, **kwargs):
       pass