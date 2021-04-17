from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Client, Contract, Event
from .serializers import (ClientSerializer, ClientListSerializer, ContractSerializer,
                          ContractListSerializer, EventSerializer, EventListSerializer)
from .permissions import ClientPermission, ContractPermission, EventPermission


class CustomListMixin:
    """
    Custom List View that allows to specify a different serializer for displaying
    a list of objects. This class shall be inherited in conjuction with a viewset class.
    The parameter list_serializer_class shall be set to the serializer used for list
    display.
    """

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_list_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_list_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_list_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for the list view.
        """
        serializer_class = self.list_serializer_class
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)


class ClientViewSet(CustomListMixin, viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated, ClientPermission]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    list_serializer_class = ClientListSerializer

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

    @action(methods=['POST'], detail=True)
    def add_contract(self, request, pk=None):
        self.check_object_permissions(request, self.get_object())
        serializer = ContractSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(client=self.get_object())
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ContractViewSet(CustomListMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated, ContractPermission]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    list_serializer_class = ContractListSerializer

    @action(methods=['POST'], detail=True)
    def add_event(self, request, pk=None):
        self.check_object_permissions(request, self.get_object())
        serializer = EventSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.validate_contract(pk)
        serializer.save(contract=self.get_object())     
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EventViewSet(CustomListMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated, EventPermission]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    list_serializer_class = EventListSerializer
