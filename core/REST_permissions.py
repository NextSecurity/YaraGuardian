from rest_framework import permissions
from rest_framework.permissions import BasePermission
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group


def group_owner(request):
    group_name = request.resolver_match.kwargs.get('group_name')

    try:
        group = Group.objects.get(name=group_name)
    except ObjectDoesNotExist:
        pass
    else:
        if request.user == group.groupmeta.owner:
            return True

    return False


def group_admin(request):
    group_name = request.resolver_match.kwargs.get('group_name')

    try:
        group = Group.objects.get(name=group_name)
    except ObjectDoesNotExist:
        pass
    else:
        if request.user == group.groupmeta.owner:
            return True
        elif request.user in group.groupmeta.admins.all():
            return True

    return False


def group_member(request):
    group_name = request.resolver_match.kwargs.get('group_name')

    if request.user.groups.filter(name=group_name).exists():
        return True

    return False


class IsGroupMember(BasePermission):

    def has_permission(self, request, view):
        return group_member(request)


class IsGroupMemberOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if group_member(request):
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True

        return False


class IsGroupAdmin(BasePermission):

    def has_permission(self, request, view):
        if group_member(request) and group_admin(request):
            return True

        return False


class IsGroupAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if group_member(request) and group_admin(request):
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True

        return False


class IsGroupAdminOrAddMethod(BasePermission):

    def has_permission(self, request, view):
        if group_member(request) and group_admin(request):
            return True
        elif request.method == 'POST':
            return True

        return False


class IsGroupOwner(BasePermission):

    def has_permission(self, request, view):
        if group_member(request) and group_owner(request):
            return True

        return False


class IsGroupOwnerOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if group_member(request) and group_owner(request):
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True

        return False
