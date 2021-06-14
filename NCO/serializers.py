from rest_framework.authtoken.admin import User
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from NCO.models import News, NewsImage, Law, NewsFavourite, Public


class NewsSerializer(ModelSerializer):
    is_favourite = SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'short_description', 'description', 'link', 'image', 'created_date', 'is_favourite']

    def get_is_favourite(self, obj):
        user = self.context['user']

        if user.is_anonymous:
            return False
        elif NewsFavourite.objects.filter(user=user, news=obj):
            return True


class NewsDetailSerializer(ModelSerializer):
    images = SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'short_description', 'link', 'images']

    def get_images(self, obj):
        return NewsImage.objects.filter(news=obj).values_list('image', flat=True)


class LawSerializer(ModelSerializer):
    class Meta:
        model = Law
        fields = ['id', 'title', 'description', 'type', 'created_date']


class LawTypeSerializer(ModelSerializer):
    class Meta:
        model = Law
        fields = ['id', 'title', 'description']


class PublicSerializer(ModelSerializer):
    class Meta:
        model = Public
        fields = ['id', 'title', 'type', 'description', 'created_date']


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'last_login']