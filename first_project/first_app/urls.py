from django.urls import path
from . import views
from .views import PersonList

app_name = 'first_app'

urlpatterns = [
    path('hello', views.index, name='index'),
    # path('page/<str:user_name>', views.get_user_page, name='get_user_page'),
    path('list', PersonList.as_view()),
]