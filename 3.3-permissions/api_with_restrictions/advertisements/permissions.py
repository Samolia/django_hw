from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthOrReadOnly(BasePermission):
    @staticmethod
    def check(request):
        if request.method is SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_permission(self, request, view):
        return self.check(request)

    def has_object_permission(self, request, view, obj):
        return self.check(request)


class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.creator or request.user.is_superuser


