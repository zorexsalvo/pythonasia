from .models import NavigationItem


def navigation(request):
    """
    Context processor to make navigation items available in all templates.
    Returns only top-level active navigation items with their active children.
    """
    nav_items = NavigationItem.objects.filter(is_active=True, parent=None).prefetch_related("children")

    return {"navigation_items": nav_items}
