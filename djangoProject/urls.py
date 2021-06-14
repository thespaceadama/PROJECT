from django.contrib import admin
from django.urls import path
from NCO import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/news/', views.NewsListApiView.as_view()),
    path('api/v1/news/<int:id>/', views.NewsDetailApiView.as_view()),
    path('api/v1/laws/', views.LawsListApiView.as_view()),
    path('api/v1/laws/<int:type>/', views.LawsFilterApiView.as_view()),
    path('api/v1/law/<int:id>/', views.LawDetailApiView.as_view()),
    path('api/v1/publics/', views.PublicListApiView.as_view()),
    path('api/v1/publics/<int:type>/', views.PublicTypApiView.as_view()),
    path('api/v1/public/<int:id>/', views.PublicDetailApiView.as_view()),
    path('api/v1/users/', views.UsersListApiView.as_view()),
    path('api/v1/register/', views.RegisterApiView.as_view()),
    path('api/v1/auth/', views.LoginApiView.as_view())
]
