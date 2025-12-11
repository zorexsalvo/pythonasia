from django.contrib import admin

from .models import NavigationItem, Page


class NavigationItemAdmin(admin.ModelAdmin):
    list_display = ["title", "parent", "page", "external_url", "order", "is_active"]
    list_filter = ["is_active", "parent"]
    search_fields = ["title", "page__title"]
    list_editable = ["order", "is_active"]
    ordering = ["parent__order", "parent__title", "order", "title"]

    fieldsets = (
        (None, {"fields": ("title", "parent", "order", "is_active")}),
        (
            "Link To",
            {"fields": ("page", "external_url"), "description": "Choose either a page or external URL (not both)"},
        ),
    )


admin.site.register(Page)
admin.site.register(NavigationItem, NavigationItemAdmin)
