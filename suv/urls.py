from rest_framework.authtoken.views import obtain_auth_token
from django.contrib import admin
from django.urls import path
from asosiy.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Suv API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="suvlar@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('suvlar/',SuvlarAPIView.as_view()),
    path('suv/<int:pk>/',SuvAPIView.as_view()),
    path('mijozlar/',MijozlarAPIView.as_view()),
    path('mijoz/<int:pk>/',MijozAPIView.as_view()),
    path('adminlar/',AdminlarAPIView.as_view()),
    path('admin/<int:pk>/',AdminAPIView.as_view()),
    path('haydovchilar/',HaydovchilarAPIView.as_view()),
    path('haydovchi/<int:pk>/',HaydovchiAPIView.as_view()),
    path('buyurtmalar/',BuyurtmalarAPIView.as_view()),
    path('get_token/', obtain_auth_token),
    path('docs/',schema_view.with_ui("swagger", cache_timeout=0)),


]
