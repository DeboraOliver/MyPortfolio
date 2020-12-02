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
#
# class PostFilter(django_filters.FilterSet):
#     #name = django_filters.CharFilter(lookup_expr='iexact')
#     stack = django_filters.ModelMultipleChoiceFilter(queryset=Post.objects.all(),)
#
#     class Meta:
#         model = Post
#         fields = ['stack']