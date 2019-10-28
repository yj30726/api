from .models import Post #모델을 기반으로 직렬화 시키기 위해
from rest_framework import serializers #rest_framework 로부터 import해줍니다.

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post #post 모델을 기반으로 직렬화 시킵니다. 
        fields = ('title', 'body') #튜플의 형태로 사용하는 것을 권장한다고 합니다. 

#형태는 modelform과 비슷하죠? 