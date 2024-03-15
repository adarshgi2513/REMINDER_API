from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    time = models.CharField(max_length=20)
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\nTime: {self.time}\nDate: {self.date}\nMessage: {self.message}"

    
