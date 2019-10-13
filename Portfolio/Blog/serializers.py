from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["title", "author", "date", "text", "tag", "thumbnail"]


class BlogFilterSerializer(serializers.Serializer):
    """
    Used exclusively to validate date when filtering
    """
    year_regex = r"^\d{4}$"
    year = serializers.RegexField(regex=year_regex, required=False)
    months = [
        "01", "02", "03", "04", "05", "06",
        "07", "08", "09", "10", "11", "12",
    ]
    month = serializers.ChoiceField(choices=months, required=False)
    tags = Blog.tags_options
    tag = serializers.ChoiceField(choices=tags, required=False)


class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["title", "author", "date", "tag", "thumbnail", "id"]
