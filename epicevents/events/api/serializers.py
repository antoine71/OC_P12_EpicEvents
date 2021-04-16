from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import Client, Contract, Event


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'
        read_only_fields = [
            'id',
            'converted',
            'sales_contact',
            'date_created',
            'date_updated',
        ]


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = '__all__'
        read_only_fields = [
            'id',
            'client',
            'date_created',
            'date_updated',
        ]


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = [
            'support_contact',
            'contract',
            'date_created',
            'date_updated',
        ]

    def validate_contract(self, contract_pk):
        contract = Contract.objects.get(pk=contract_pk)
        if Event.objects.filter(contract=contract).exists():
            raise ValidationError('An event already exists for this contract', code='unique')
