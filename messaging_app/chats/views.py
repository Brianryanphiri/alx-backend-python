from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer
from .permissions import IsParticipantOfConversation

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [IsParticipantOfConversation]

    def get_queryset(self):
        conversation_id = self.request.query_params.get('conversation_id')
        if not conversation_id:
            raise PermissionDenied(detail="conversation_id is required.", code=status.HTTP_403_FORBIDDEN)
        return Message.objects.filter(conversation_id=conversation_id, conversation__participants=self.request.user)

    def perform_create(self, serializer):
        conversation_id = self.request.data.get('conversation')
        if not conversation_id:
            raise PermissionDenied(detail="conversation is required.", code=status.HTTP_403_FORBIDDEN)
        # Optionally, add more permission checks here
        serializer.save(owner=self.request.user)
