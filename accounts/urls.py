from . import views
from django.urls import path,include




app_name = 'accounts'
urlpatterns = [
    path('', views.AllUsers.as_view(),name='users'),
    path('comments/', views.AllComments.as_view(),name='comments'),
]
