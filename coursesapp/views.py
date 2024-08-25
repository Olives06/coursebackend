from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from coursesapp.models import Course, CourseInstance
from coursesapp.serializers import CourseSerializer, CourseInstanceSerializer

class CourseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing course instances.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def destroy(self, request, *args, **kwargs):
        """
        DELETE /api/courses/24
        Delete a course with ID = 24
        """
        course = get_object_or_404(Course, pk=kwargs['pk'])
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CourseInstanceViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing course delivery instances.
    """
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.kwargs.get('year')
        semester = self.kwargs.get('semester')
        course_id = self.kwargs.get('course_id')
        if year and semester and course_id:
            queryset = queryset.filter(year=year, semester=semester, course_id=course_id)
        elif year and semester:
            queryset = queryset.filter(year=year, semester=semester)
        return queryset

    def destroy(self, request, *args, **kwargs):
        """
        DELETE /api/instances/YYYY/SEM/ID
        Delete an instance of a course with the specified ID, year, and semester
        """
        year = kwargs.get('year')
        semester = kwargs.get('semester')
        course_id = kwargs.get('pk')
        instance = get_object_or_404(CourseInstance, course_id=course_id, year=year, semester=semester)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='(?P<year>[0-9]{4})/(?P<semester>[0-9]+)/(?P<course_id>[0-9]+)')
    def retrieve_instance(self, request, year=None, semester=None, course_id=None):
        """
        GET /api/instances/YYYY/SEM/ID
        View detailed information about an instance of a course ID = 19, delivered in YYYY=2023, and semester = 1
        """
        instance = get_object_or_404(CourseInstance, year=year, semester=semester, course_id=course_id)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
