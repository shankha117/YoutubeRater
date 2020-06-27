from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from .models import Video, Rating
from rest_framework.decorators import action
from .serializers import VideoSerializer, RatingSerializer, UserSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = VideoSerializer
    permission_classes = (permissions.AllowAny,)

    @action(methods=['POST'], detail=True)
    def rate_video(self, request, pk=None):
        if 'stars' in request.data:
            video = Video.objects.get(id=pk)
            stars = request.data['stars']
            comments = request.data['comments']
            user = request.user
            print(user,comments,stars,video)
            try:
                rating = Rating.objects.get(user=user.id, video=video.id)
                rating.stars = stars
                rating.comments = comments
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {"message": 'rating updated', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
            except Exception:
                print(" IA M EXCEPTION")
                rating = Rating.objects.create(user=user, video=video, stars=stars, comments=comments)
                serializer = RatingSerializer(rating, many=False)
                response = {"message": 'rating created', 'result': serializer.data}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {"message": 'please add stars'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = RatingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        response = {'message': 'Rating can not be delted'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
