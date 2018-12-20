from django.urls import path, include
from rest_framework import routers
from views.CategoriaView import CategoriaViewSet

router = routers.DefaultRouter()
router.register('categorias', CategoriaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('admin/', admin.site.urls),
    #path('admin/doc/', include('django.contrib.admindocs.urls')),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]
