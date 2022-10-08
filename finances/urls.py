
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from releases.views.receitas_viewset import ReceitasViewSet
from releases.views.despesas_viewset import DespesasViewSet
from releases.views.lancamentos_mensais_viewset import DespesasMensaisViewSet, ReceitasMensaisViewSet
from releases.views.resumo_viewset import ResumoViewSet

route = routers.DefaultRouter()
route.register(r'receitas', ReceitasViewSet, basename='Receitas')
route.register(r'despesas', DespesasViewSet, basename='Despesas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('despesas/<str:ano>/<str:mes>/', DespesasMensaisViewSet.as_view()),
    path('receitas/<str:ano>/<str:mes>/', ReceitasMensaisViewSet.as_view()),
    path('resumo/<str:ano>/<str:mes>/', ResumoViewSet.as_view(), name='Resumo')
]
