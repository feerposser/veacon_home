from django.db import models


class ContactModel(models.Model):
    date_time = models.DateTimeField(auto_now_add=True, editable=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=250, null=True, blank=True)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
