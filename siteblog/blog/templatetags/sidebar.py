from django import template

from blog.models import Post, Tag

register = template.Library()


@register.inclusion_tag('blog/popular_posts_tpl.html')
def show_popular_posts(cnt=3):
    popular_posts = Post.objects.order_by('-views')[:cnt]
    return {'popular_posts': popular_posts}


@register.inclusion_tag('blog/tags_tpl.html')
def show_tags():
    tags = Tag.objects.all()
    return {'tags': tags}


@register.inclusion_tag('blog/search_tpl.html')
def show_search():
    pass
