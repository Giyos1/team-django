from django.db import models


class Authors(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    biography = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    photo = models.ImageField(upload_to='authors/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'authors'
        ordering = ['birth_date']
