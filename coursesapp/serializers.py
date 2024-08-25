from rest_framework import serializers
from coursesapp.models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'course_code', 'description']

class CourseInstanceSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)

    class Meta:
        model = CourseInstance
        fields = ['id', 'course', 'course_title', 'year', 'semester', 'code']
        read_only_fields = ['course_title']
