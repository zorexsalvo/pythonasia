from django.db import models
from tinymce.models import HTMLField


class Announcement(models.Model):
    MODAL_SIZES = [
        ("md", "Medium (default)"),
        ("lg", "Large"),
        ("xl", "Extra Large"),
    ]

    title = models.CharField(max_length=255)
    content = HTMLField()
    modal_size = models.CharField(
        max_length=10,
        choices=MODAL_SIZES,
        default="md",
        help_text="Width of the announcement modal",
    )
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_latest_published(cls):
        """Get the latest published announcement."""
        return cls.objects.filter(is_published=True).order_by("-created_at").first()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"


class ButtonCTA(models.Model):
    label = models.CharField(max_length=100)
    url = models.URLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label

    @classmethod
    def get_active(cls):
        """Get the first active button CTA."""
        return cls.objects.filter(is_active=True).first()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Button CTA"
        verbose_name_plural = "Button CTAs"


class RibbonCTA(models.Model):
    message = models.CharField(max_length=255)
    cta_text = models.CharField(max_length=100, default="LEARN MORE")
    cta_url = models.URLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    @classmethod
    def get_active(cls):
        """Get the first active ribbon CTA."""
        return cls.objects.filter(is_active=True).first()

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Ribbon CTA"
        verbose_name_plural = "Ribbon CTAs"
