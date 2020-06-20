from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
