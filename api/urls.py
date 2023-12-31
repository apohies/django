from django.urls import path,include
from rest_framework import routers
from api import views


router= routers.DefaultRouter()
router.register(r'programmers',views.ProgrammerViewSet)

urlpatterns = [ path('',include(router.urls)),
                path('funder/', views.lefdepart),
                path('crearusuario/', views.CrearUsuario)
                ]



