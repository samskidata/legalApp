from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # Add any other fields you need for the user model

    def __str__(self):
        return self.username

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='uploads/', null=True, blank=True, 
                            validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'txt', 'csv'])])

    def __str__(self):
        return self.content
