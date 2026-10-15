class OwnerCreateMixin:
    """Reusable mixin that automatically sets the logged-in user as the resource owner."""
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
