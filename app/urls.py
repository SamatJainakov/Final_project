from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, schema


urlpatterns = [
    path('image/', views.ImageListCreateAPIView.as_view()),
    path('category/', views.CategoryListCreateAPIView.as_view()),
    path('image/<int:pk>/', views.ImageRetrieveUpdateDestroyAPIView.as_view()),
    path('swagger/', schema.schema_view.with_ui('swagger', cache_timeout=0)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
