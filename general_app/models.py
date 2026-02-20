from django.db import models

class Contact(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    message_subject = models.CharField(max_length=200)
    message_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user_ip = models.GenericIPAddressField()

    def __str__(self):
        return self.message_subject


class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=200)
    password_repetition = models.CharField(max_length=200)

    def __str__(self):
        return self.user_email