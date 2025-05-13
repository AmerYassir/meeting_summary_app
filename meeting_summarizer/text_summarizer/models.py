from django.db import models

class UploadedText(models.Model):
    text_file = models.FileField(upload_to='uploads/')  # For file uploads
    text_content = models.TextField(blank=True, null=True) # If you read the content
    summary = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Uploaded on {self.upload_date.strftime('%Y-%m-%d %H:%M')}"