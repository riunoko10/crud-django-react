
from django.urls import path, include
from tasks import views
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register(r'tasks', views.TaskListView, 'tasks')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/', include_docs_urls(title='Task API', public=True)),
]
