from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_view),
    path('<int:personal_id>', views.person_view)
]