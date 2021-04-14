from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from events.models import Client, Contract, Event
from .serializers import ClientSerializer, ContractSerializer, EventSerializer


class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

    @action(methods=['POST'], detail=True)
    def add_contract(self, request, pk=None):
        serializer = ContractSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(client=self.get_object())
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ContractViewSet(viewsets.ModelViewSet):

    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    @action(methods=['POST'], detail=True)
    def add_event(self, request, pk=None):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validate_contract(pk)
        serializer.save(contract=self.get_object())
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EventViewSet(viewsets.ModelViewSet):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
