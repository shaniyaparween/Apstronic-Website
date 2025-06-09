from django.db import models

class Domain(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    points = models.TextField(help_text="Use line breaks for list items")

    def __str__(self):
        return self.title



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
