from django import template

register = template.Library()


@register.simple_tag
def is_liked_by_user(post, user):
    result = post.is_liked_by_user(user)
    print("[DEBUG] post.is_liked_by_user(user): ", result)
    return result
