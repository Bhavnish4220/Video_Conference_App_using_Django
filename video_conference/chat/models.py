from django.db import models

class MyFile(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    file = models.FileField(upload_to='myfile')
    date=models.DateTimeField(auto_now_add=True)