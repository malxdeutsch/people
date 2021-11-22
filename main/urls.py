from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_view),
    path('<int:person_id>', views.person_view)
]