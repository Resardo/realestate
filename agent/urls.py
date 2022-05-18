from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('search/<slug:slug>/', views.agent_properties, name='agent_properties'),
    path('ourteam/', views.agent_all, name='agent_all'),
]