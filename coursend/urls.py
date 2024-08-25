from django.urls import path, include
from rest_framework.routers import DefaultRouter
from coursesapp.views import CourseViewSet, CourseInstanceViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'course-instances', CourseInstanceViewSet, basename='courseinstance')

urlpatterns = [
    path('api/', include(router.urls)),
]
