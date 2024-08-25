from django.db import models

class Course(models.Model):
    """
    Represents a course in the system.
    """
    title = models.CharField(max_length=255)
    course_code = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.course_code})"


class CourseInstance(models.Model):
    """
    Represents a specific instance of a course offered in a particular year and semester.
    """
    course = models.ForeignKey(Course, related_name='instances', on_delete=models.CASCADE)
    year = models.CharField(max_length=4)
    semester = models.PositiveSmallIntegerField()
    code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.course.title} - {self.year}-{self.semester} ({self.code})"
