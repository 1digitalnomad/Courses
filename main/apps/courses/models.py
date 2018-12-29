from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, form_data):
        errors = []
        if len(form_data['name']) < 5:
            errors.append('Course name must be more than 5 characters.')
        if len(form_data['description']) < 15:
            errors.append('Course description must be more than 15 characters')
        
        print(form_data)
        return errors

    def create_course(self, form):
        self.create(
            name = form['name'],
            description = form['description']
        )

    def delete_course(self, course_id):
        b = Courses.objects.get(id=course_id)
        b.delete()


class Courses(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
