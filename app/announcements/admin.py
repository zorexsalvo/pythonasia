from django.contrib import admin

from .models import Announcement, RibbonCTA


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "modal_size", "is_published", "created_at", "updated_at")
    list_filter = ("is_published", "modal_size", "created_at")
    search_fields = ("title", "content")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Content", {"fields": ("title", "content")}),
        ("Display", {"fields": ("modal_size",)}),
        ("Status", {"fields": ("is_published",)}),
        ("Metadata", {"fields": ("created_at", "updated_at")}),
    )


@admin.register(RibbonCTA)
class RibbonCTAAdmin(admin.ModelAdmin):
    list_display = ("message", "cta_text", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("message", "cta_text")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        ("Content", {"fields": ("message", "cta_text", "cta_url")}),
        ("Status", {"fields": ("is_active",)}),
        ("Metadata", {"fields": ("created_at", "updated_at")}),
    )
