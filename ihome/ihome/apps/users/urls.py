from . import views
from django.urls import path

urlpatterns = [
    # 图形验证码: GET api/v1.0/imagecode
    path('api/v1.0/imagecode', views.ImageCodeView.as_view()),
]