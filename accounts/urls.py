from . import views
from django.urls import path,include

from rest_framework.authtoken import views as TokenView



app_name = 'accounts'
urlpatterns = [
    path('', views.AllUsers.as_view(),name='users'),
    path('comments/', views.AllComments.as_view(),name='comments'),
    path('comment/delete/<int:pk>/', views.DeleteComment.as_view(),name='del-comment'),
    path('comment/update/<int:pk>/', views.UpdateComment.as_view(),name='update-comment'),
    path('comment/create/', views.CreateComment.as_view(),name='create-comment'),
    path('api-token-auth/', TokenView.obtain_auth_token),

]
