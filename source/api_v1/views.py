from rest_framework import viewsets
from django.shortcuts import render
from api_v1.serializers import PostModelSerializer
from feed.models import PostModel
from django.http import JsonResponse
from rest_framework.permissions import BasePermission, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView

def find_post( id):
    return PostModel.objects.get(id=id)

def url_parse(str):
    return int(str.split('/')[3])


class IsAllowed(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated:
            if view.action == 'partial_update' or view.action == 'destroy':
                if find_post(url_parse(request.path)) in request.user.usr_posts.all():
                    return True
                else: return False
            else: return True
        elif view.action == 'list' or view.action == 'retrieve':
            return True
        else: return False


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAllowed]
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer

    def current_object(self):
        return self.get_object()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikeView(APIView):
    permission_classes = [IsAuthenticated]            # <-- And here

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:  
            post = find_post(url_parse(request.path))
            icon = ''
            try:
                if post.likes.filter(id=request.user.id).exists():
                    post.likes.remove(request.user)
                    icon = '<i class="bi bi-heart text-danger fs-2"></i>'
                else:
                    post.likes.add(request.user)
                    icon = '<i class="bi bi-heart-fill text-danger fs-2"></i>'
                return JsonResponse({'count': post.likes.count(), 'icon': icon})
            except:
                return JsonResponse({'error': "who knows..."})
        else:
            return JsonResponse({'error': "not authorized"})
