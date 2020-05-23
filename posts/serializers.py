from rest_framework import serializers

from posts.models import Post, Comment


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'title', 'creation_date', 'author_name', 'link', 'amount_of_upvotes')
        read_only_fields = ('amount_of_upvotes', 'link')

    def create(self, validated_data):
        post = Post(
            title=validated_data['title'],
            author_name=validated_data['author_name'],
        )
        post.save()
        post.link = f'http://127.0.0.1:8000/posts/{post.pk}'
        post.save()
        return post


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk', 'author_name', 'content', 'creation_date', 'post')
