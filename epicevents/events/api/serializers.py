from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.relations import HyperlinkedRelatedField, StringRelatedField

from ..models import Client, Contract, Event


class ClientListSerializer(serializers.ModelSerializer):

    sales_contact = serializers.StringRelatedField()

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'company_name',
            'sales_contact',
            'email',
            'converted',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:client-detail"}
        }


class ContractNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = [
            'id',
            'project_name',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:contract-detail"}
        }


class ClientSerializer(serializers.ModelSerializer):

    contracts = ContractNestedSerializer(many=True, read_only=True)
    sales_contact = StringRelatedField()

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'company_name',
            'sales_contact',
            'email',
            'phone',
            'mobile',
            'converted',
            'contracts',
            'date_created',
            'date_updated',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:client-detail"}
        }
        read_only_fields = [
            'converted',
            'sales_contact',
            'date_created',
            'date_updated',
        ]


class ClientNestedSerializer(serializers.ModelSerializer):

    sales_contact = StringRelatedField()

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'company_name',
            'sales_contact',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:client-detail"}
        }


class ContractListSerializer(serializers.ModelSerializer):

    client = ClientNestedSerializer()

    class Meta:
        model = Contract
        fields = [
            'id',
            'project_name',
            'signed',
            'amount',
            'client',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:contract-detail"}
        }


class ContractSerializer(serializers.ModelSerializer):

    client = ClientNestedSerializer(read_only=True)
    event = HyperlinkedRelatedField(view_name='api:event-detail', read_only=True)

    class Meta:
        model = Contract
        fields = [
            'id',
            'project_name',
            'signed',
            'amount',
            'payment_due_date',
            'client',
            'event',
            'date_created',
            'date_updated',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:contract-detail"}
        }
        read_only_fields = [
            'date_created',
            'date_updated',
            'event',
        ]


class EventListSerializer(serializers.ModelSerializer):

    contract = ContractNestedSerializer()
    support_contact = StringRelatedField()

    class Meta:
        model = Event
        fields = [
            'support_contact',
            'event_date',
            'completed',
            'contract',
        ]


class EventSerializer(serializers.ModelSerializer):

    contract = ContractNestedSerializer(read_only=True)
    support_contact = StringRelatedField()

    class Meta:
        model = Event
        fields = [
            'support_contact',
            'attendees',
            'event_date',
            'notes',
            'completed',
            'contract',
            'date_created',
            'date_updated',
            'url',
        ]
        extra_kwargs = {
            "url": {"view_name": "api:event-detail"}
        }
        read_only_fields = [
            'support_contact',
            'date_created',
            'date_updated',
        ]

    def validate_contract(self, contract_pk):
        contract = Contract.objects.get(pk=contract_pk)
        if Event.objects.filter(contract=contract).exists():
            raise ValidationError('An event already exists for this contract', code='unique')
