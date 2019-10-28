from django.db import models

# Create your models here.
class ClassBlog(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True) #자동으로 작성되게 설정하였습니다. 
    updated_at = models.DateTimeField(auto_now=True) #자동으로 작성되게 설정하였습니다.
    body = models.TextField()

    def __str__(self):
        return self.title