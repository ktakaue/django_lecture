from django.urls import path
from . import views
from .views import PersonList, PersonDetail

app_name = 'first_app'

urlpatterns = [
    path('hello', views.index, name='index'),
    # path('page/<str:user_name>', views.get_user_page, name='get_user_page'),
    path('get_all_persons/', views.get_all_persons, name='get_all_persons'),
    path('list', PersonList.as_view()),
    path('detail/<int:pk>/', PersonDetail.as_view()),
    # path('create/', createView.as_view()),

]