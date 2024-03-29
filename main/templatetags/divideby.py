from django import template

register = template.Library()


@register.filter
def divideby(lst, n):
    result = []
    for i in range(0, len(lst), n):
        result.append(lst[i:i + n])
    return result
