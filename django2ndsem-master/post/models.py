from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

#모델 설정은 동일합니다. 앞서 보았듯이 모델을 받아오는 형태만 다를 뿐이기 때문입니다. 
#모델을 만들어주었으니 migrate하는 과정을 해 주어야 겠죠?