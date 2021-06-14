from django.contrib.auth import authenticate
from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

from NCO.models import News, Law, Public
from NCO.serializers import NewsSerializer, NewsDetailSerializer, LawSerializer, LawTypeSerializer, PublicSerializer, \
    RegisterSerializer


class NewsListApiView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def list(self, request, *args, **kwargs):
        news = self.get_queryset()
        data = self.serializer_class(news, many=True, context={'user': request.user}).data
        return Response(data=data)


class NewsDetailApiView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    lookup_field = 'id'


class LawsListApiView(ListAPIView):
    queryset = Law.objects.all()
    serializer_class = LawSerializer


class LawsFilterApiView(ListAPIView):
    queryset = Law.objects.all()
    serializer_class = LawTypeSerializer

    def get_queryset(self):
        laws = Law.objects.filter(type=self.kwargs['type'])
        return laws


class LawDetailApiView(RetrieveAPIView):
    queryset = Law.objects.all()
    serializer_class = LawSerializer
    lookup_field = 'id'


class PublicListApiView(ListAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer


class PublicTypApiView(ListAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer

    def get_queryset(self):
        return Public.objects.filter(type=self.kwargs['type'])


class PublicDetailApiView(RetrieveAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer
    lookup_field = 'id'


class RegisterApiView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']
        password2 = request.data['password2']

        isUniqueUser = User.objects.filter(username=username).first()

        if isUniqueUser:
            return Response(data={'message': 'This user is already registered!'})
        elif password != password2:
            return Response(data={'message': 'Passwords not valid!'})

        user = User.objects.create_user(
            username=username,
            password=password,
            email='a@b.com'
        )

        user.save()
        Token.objects.create(user=user)

        return Response(data={'message': 'ok'})


class UsersListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginApiView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)

        if not user:
            return Response(data={'message': 'username or password not valid!'})

        tokens = Token.objects.filter(user=user).first()
        tokens.delete()
        token = Token.objects.create(user=user)

        return Response(data={'username': user.username, 'token': token.key})