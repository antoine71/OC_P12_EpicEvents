from django_filters import rest_framework as filters
from ..models import Contract, Event, Client


class ClientFilter(filters.FilterSet):

    sort_by = filters.CharFilter(
        method='filter_sort_by',
        label="Sort by a given value (compane_name, -company_name, etc.)",
    )

    def filter_sort_by(self, queryset, name, value):
        values = value.lower().split(',')
        return queryset.order_by(*values)

    class Meta:
        model = Client
        fields = [
            'id',
            'first_name',
            'last_name',
            'company_name',
            'sales_contact',
            'email',
            'converted'
        ]


class ContractFilter(filters.FilterSet):
    min_amount = filters.NumberFilter(field_name="amount", lookup_expr='gte')
    max_amount = filters.NumberFilter(field_name="amount", lookup_expr='lte')

    sort_by = filters.CharFilter(
        method='filter_sort_by',
        label="Sort by a given value (amount, -amount, etc.)",
    )

    def filter_sort_by(self, queryset, name, value):
        values = value.lower().split(',')
        return queryset.order_by(*values)

    class Meta:
        model = Contract
        fields = [
            'id',
            'project_name',
            'signed',
            'min_amount',
            'max_amount',
            'client__id',
            'client__sales_contact',
            ]


class EventFilter(filters.FilterSet):

    min_attendees = filters.NumberFilter(field_name="attendees", lookup_expr='gte')
    max_attendees = filters.NumberFilter(field_name="attendees", lookup_expr='lte')

    sort_by = filters.CharFilter(
        method='filter_sort_by',
        label="Sort by a given value (event_date, -event_date, etc.)",
    )

    def filter_sort_by(self, queryset, name, value):
        values = value.lower().split(',')
        return queryset.order_by(*values)

    class Meta:
        model = Event
        fields = [
            'support_contact',
            'attendees',
            'event_date',
            'completed',
            'contract__id',
            'contract__project_name',
        ]
