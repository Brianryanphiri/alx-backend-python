from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsParticipantOfConversation

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]

    def get_queryset(self):
        conversation_id = self.kwargs.get('conversation_id')
        if not conversation_id:
            return Message.objects.none()

        # Filter messages only for this conversation
        queryset = Message.objects.filter(conversation__id=conversation_id)

        # Check if current user is participant in this conversation
        if not queryset.exists() or self.request.user not in queryset.first().conversation.participants.all():
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied(detail="You do not have permission to access this conversation.")

        return queryset
