from django.urls import path,include
from rest_framework import routers
from api.views import views
from api.views import profileviews



router= routers.DefaultRouter()
router.register(r'programmers',views.ProgrammerViewSet)

urlpatterns = [ path('',include(router.urls)),
                path('funder/', views.lefdepart),
                path('crearusuario/', views.CrearUsuario),
                path('mensaje/', profileviews.mensaje),
                path('code',profileviews.CrearSubjet),
                path('mongos',profileviews.getSubjets)
                ]



