from django.urls import path, include
from django.views.generic import RedirectView

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'creators', views.CreatorViewSet)
router.register(r'ability', views.AbilityViewSet)
router.register(r'characters', views.CharacterViewSet, 'characters')

# Wire up API's using automatic URL routing
# Include login urls for browsable API
urlpatterns = [
    path('', views.CharacterListView.as_view()),
    # Redirect To Default EndPoint
    # path(r'', RedirectView.as_view(url='/api/')),
    
    # REST
    path('api/', include(router.urls)), # Base End point -> http://127.0.0.1:8000/api

    # CharacterViewSet
    path('api/characters/', views.CharacterViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('api/characters/<str:pk>/', views.CharacterViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]