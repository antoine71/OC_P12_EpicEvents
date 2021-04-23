from datetime import datetime
import logging

from django.utils.timezone import make_aware
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ..models import Client, Contract, Event
from .serializers import (ClientSerializer, ClientListSerializer, ContractSerializer,
                          ContractListSerializer, EventSerializer, EventListSerializer)
from .permissions import ClientPermission, ContractPermission, EventPermission
from .filters import ContractFilter, EventFilter


logger = logging.getLogger(__name__)


class CustomListMixin:
    """
    Custom List View that allows to specify a different serializer for displaying
    a list of objects. This class shall be inherited in conjuction with a viewset class.
    The parameter list_serializer_class shall be set to the serializer used for list
    display.
    """

    def list(self, request, filter=None, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if filter is not None:
            queryset = queryset.filter(**filter)
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


class customUpdateMixin(mixins.UpdateModelMixin):
    """
    Custom Update View that allows to update the field date_updated.
    """

    def perform_update(self, serializer):
        serializer.save(date_updated=make_aware(datetime.now()))


class ClientViewSet(CustomListMixin, customUpdateMixin, viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated, ClientPermission]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    list_serializer_class = ClientListSerializer
    filterset_fields = [
        'id',
        'first_name',
        'last_name',
        'company_name',
        'sales_contact',
        'email',
        'converted'
        ]

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)

    @action(methods=['POST', 'GET'], detail=True)
    def contracts(self, request, pk=None):
        self.check_object_permissions(request, self.get_object())
        if request.method == 'POST':
            client = self.get_object()
            serializer = ContractSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save(client=client)
            if not client.converted:
                client.converted = True
                client.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            queryset = Contract.objects.filter(client__pk=pk)
            page = self.paginate_queryset(queryset)
            serializer = ContractListSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

    @action(methods=['GET'], detail=False)
    def me(self, request):
        logger.error(f'{request.user}')
        logger.error('Something went wrong!')
        return self.list(request=request, filter={'sales_contact': request.user})


class ContractViewSet(CustomListMixin,
                      mixins.RetrieveModelMixin,
                      customUpdateMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated, ContractPermission]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    list_serializer_class = ContractListSerializer
    filterset_class = ContractFilter

    @action(methods=['GET', 'POST'], detail=True)
    def events(self, request, pk=None):
        self.check_object_permissions(request, self.get_object())
        if request.method == 'POST':
            serializer = EventSerializer(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.validate_contract(pk)
            serializer.save(contract=self.get_object())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            queryset = Event.objects.filter(contract=pk)
            page = self.paginate_queryset(queryset)
            serializer = EventListSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

    @action(methods=['GET'], detail=False)
    def me(self, request):
        return self.list(request=request, filter={'client__sales_contact': request.user})

    @action(methods=['GET'], detail=False)
    def prospects(self, request):
        return self.list(request=request, filter={'converted': False})


class EventViewSet(CustomListMixin,
                   mixins.RetrieveModelMixin,
                   customUpdateMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):

    permission_classes = [IsAuthenticated, EventPermission]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    list_serializer_class = EventListSerializer
    filterset_class = EventFilter

    @action(methods=['GET'], detail=False)
    def me(self, request):
        return self.list(request=request, filter={'support_contact': request.user})
