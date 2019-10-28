#앱 내의 urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('list', views.BlogView.as_view(), name='list'), #as_view => 앞서서 정의된 클래스의 메소드임. 함수형태로 적어야 하는 규칙때문에 저 함수를 씁니다.
    path('newblog/', views.BlogCreate.as_view(), name='new'),
    path('detail/<int:pk>', views.BlogDetail.as_view(), name='detail'),
    path('update/<int:pk>', views.BlogUpdate.as_view(), name='change'),
    path('delete/<int:pk>', views.BlogDelete.as_view(), name='del'),
]