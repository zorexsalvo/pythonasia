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
