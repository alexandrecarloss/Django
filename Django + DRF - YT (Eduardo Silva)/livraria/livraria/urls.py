from django.contrib import admin
from django.urls import path, include
from core import views

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'editoras', views.EditoraViewSet)
router.register(r'autores', views.AutorViewSet)
router.register(r'livros', views.LivroViewSet)
router.register(r'compras', views.CompraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Open API 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Autenticação
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Outros endpoints
    path('api/teste/', views.teste, name='teste'),
    path('api/categorias-class/', views.CategoriaView.as_view()),
    path('api/categorias-class/<int:id>/', views.CategoriaView.as_view()),
    path('api/categorias-apiview/', views.CategoriasList.as_view()),
    path('api/categorias-apiview/<int:id>/', views.CategoriaDetail.as_view()),
    path('api/categorias-generic/', views.CategoriasListGeneric.as_view()),
    path('api/categorias-generic/<int:id>/', views.CategoriaDetailGeneric.as_view()),
    path('api/', include(router.urls)),
]
