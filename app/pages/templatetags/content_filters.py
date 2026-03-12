import re

from django import template
from django.utils.html import mark_safe

register = template.Library()


def _replace_btn_link(match):
    attrs = match.group(1)
    text = match.group(2)

    if "|btn" not in text:
        return match.group(0)

    clean_text = text.replace("|btn", "").strip()

    if "class=" in attrs:
        attrs = re.sub(r'class=["\']([^"\']*)["\']', r'class="\1 btn btn-primary"', attrs)
    else:
        attrs += ' class="btn btn-primary"'

    return f"<a {attrs}>{clean_text}</a>"


@register.filter
def render_buttons(value):
    """Convert links with |btn marker in their text to button-styled links.

    Usage in TinyMCE: set link text to "Click here|btn"
    Output: <a href="..." class="btn btn-primary">Click here</a>
    """
    result = re.sub(r"<a\s+([^>]+)>([^<]*\|btn[^<]*)</a>", _replace_btn_link, value)
    return mark_safe(result)
