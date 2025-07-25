from rest_framework import permissions

class IsParticipantOfConversation(permissions.BasePermission):
    """
    Allow access only if user is authenticated and participant of the conversation.
    """

    def has_permission(self, request, view):
        # Allow only authenticated users
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Check if user is participant of the conversation
        is_participant = obj.conversation.participants.filter(id=request.user.id).exists()
        if request.method in permissions.SAFE_METHODS:
            return is_participant
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return is_participant
        return False
