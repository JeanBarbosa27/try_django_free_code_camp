from django import template

register = template.Library()

@register.simple_tag
def link_is_active(request, url):
    is_home_url = request.path == '/' and request.path == url
    has_same_parent = url.split('/')[1] == request.path.split('/')[1]

    if is_home_url:
        return 'active'
    if has_same_parent:
        return 'active'

    return ''

@register.simple_tag
def content_max_length(value, max_length):
    return f"{value[:max_length]}..."
