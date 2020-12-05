import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):

    class Meta:
        model = Post
        fields = ['stack']

    def __init__(self, *args, **kwargs):
        super(PostFilter, self).__init__(*args, **kwargs)
        self.filters['stack'].extra.update(
            {'empty_label': 'All'})
