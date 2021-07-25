from django.urls import path

from .views import *

urlpatterns = [
    path('', news, name='home'),
    path('category/<int:category_id>/', get_category_news, name='category'),
]