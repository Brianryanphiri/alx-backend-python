from rest_framework import permissions
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Custom permission to allow only participants of a conversation to access messages.
    Also requires user to be authenticated.
    """

    def has_permission(self, request, view):
        # Allow only authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Only allow participants to view/edit/delete
        # Assuming `obj.conversation` is the conversation the message belongs to
        # and `conversation.participants` is a queryset/list of users
        return request.user in obj.conversation.participants.all()
