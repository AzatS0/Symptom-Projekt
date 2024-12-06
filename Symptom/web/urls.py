from django.urls import path
from . import views

urlpatterns = [
    path('', views.symptom_prediction, name='symptom_prediction'),
]
