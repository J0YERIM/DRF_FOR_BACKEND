from rest_framework import serializers
from .models import Post, Comment
from users.serializers import ProfileSerializer


# 게시글 시리얼라이저에 댓글 시리얼라이저가 포함되므로 댓글 시리얼라이저가 더 위에 선언 되야 함 
class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ["pk", "profile", "post", "text"]


class CommentCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ["post", "text"]


# PostSerializer와 PostCreateSerializer 따로 해줘야 함!
# 사용자가 입력할 때 serializer할 필드와 서버가 deserializer할 때 필드가 다르기 때문
class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) # nested serializer
    # 기본적으로 profile 필드에는 profile의 pk값만 나타나게 됨
    # 해당 글 작성자의 실제 프로필 정보를 알고 싶은 것이기 때문에, 시리얼라이저 내에 또 다른 시리얼라이저를 넣어서 이중으로 연결되는 구조로 작성해야 함
    # 이와 같은 형태를 nested serializer라고 한다
    comments = CommentSerializer(many=True, read_only=True) # 댓글 시리얼라이저를 포함하여 댓글 추가, many=True를 통해 다수의 댓글 포함
    
    class Meta:
        model = Post
        fields = ["pk", "profile", "title", "body", "image", "published_date", "likes", "comments"]


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "category", "body", "image"]