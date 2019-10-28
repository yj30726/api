#프로젝트 내의 urls.py

from django.contrib import admin
from django.urls import path, include
import classcrud.urls
import classcrud.views
import post.urls
from rest_framework import urls 
from rest_framework.authtoken.views import obtain_auth_token # 추가


urlpatterns = [
    path('admin/', admin.site.urls),
    path('classcrud/', include(classcrud.urls)),
    path('', include(post.urls)),
    path('userpost/', include('userpost.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
]
