from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .views import Register_list
from .views import postlist,postdetail,comment_view


urlpatterns = [
    path('login/',TokenObtainPairView.as_view()),
    path('login/refresh/',TokenRefreshView.as_view()),
    path('register/',Register_list.as_view()),
    path('post/',postlist.as_view()),
    path('post/<int:pk>/',postdetail.as_view()),
    path('comment/',comment_view.as_view()),

]
