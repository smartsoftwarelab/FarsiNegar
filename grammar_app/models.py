from django.db import models

class QuickEdit(models.Model):
    input_text = models.TextField()
    document_title = models.CharField(max_length=200)
    corrected_text = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.document_title


class DetailedEdit(models.Model):
    content = models.TextField()
    document_title = models.CharField(max_length=200)
    error_list = models.JSONField(default=list)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.document_title