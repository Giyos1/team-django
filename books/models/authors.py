from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'authors'
        ordering = ['birth_date']
