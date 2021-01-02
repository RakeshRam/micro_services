from django.urls import path, include
from django.views.generic import RedirectView

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'creators', views.CreatorViewSet)
router.register(r'ability', views.AbilityViewSet)
router.register(r'characters', views.CharacterViewSet)

# Wire up API's using automatic URL routing
# Include login urls for browsable API
urlpatterns = [
    # Redirect To Default EndPoint
    path(r'', RedirectView.as_view(url='/api/')),
    
    # REST
    path('api/', include(router.urls)), # Base End point -> http://127.0.0.1:8000/api
]