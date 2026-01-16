from django.db import models

class Tags(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        db_table = "tags"
        ordering = ['name']

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    enrollment = models.BigIntegerField(default=0)
    description = models.TextField(blank=True)
    course_price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(Tags, related_name='courses')
    class Meta:
        db_table = "course"


class CachedQuery(models.Model):
    token = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='cached_tokens')

    class Meta:
        db_table = "cached_query"
        indexes = [
            models.Index(fields=['token']),
        ]
    def __str__(self):
        return f'{self.token}-- {self.course}'