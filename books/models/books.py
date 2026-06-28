from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    author = models.ForeignKey("Authors", on_delete=models.SET_NULL, null=True, blank=True)

    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
