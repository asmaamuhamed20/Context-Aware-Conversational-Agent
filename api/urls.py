from django.urls import path
from . import views

urlpatterns = [
    path('invoke/', views.AgentInvokeView.as_view(), name='agent_invoke'),
]