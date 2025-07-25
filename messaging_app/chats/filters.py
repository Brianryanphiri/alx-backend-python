import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    start_date = django_filters.DateTimeFilter(field_name="created_at", lookup_expr='gte')
    end_date = django_filters.DateTimeFilter(field_name="created_at", lookup_expr='lte')
    participant = django_filters.CharFilter(method='filter_participant')

    class Meta:
        model = Message
        fields = ['start_date', 'end_date', 'participant']

    def filter_participant(self, queryset, name, value):
        return queryset.filter(conversation__participants__username=value)
