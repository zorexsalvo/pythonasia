from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField


class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    content = HTMLField()
    is_published = models.BooleanField(default=False)
    meta_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("pages:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Page"
        verbose_name_plural = "Pages"


class NavigationItem(models.Model):
    """Navigation item that can be top-level or a child (supports 1 level nesting only)"""

    title = models.CharField(max_length=100)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        help_text="Parent navigation item (leave empty for top-level items)",
    )
    page = models.ForeignKey(
        Page,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Link to a page (optional if this is a dropdown parent)",
    )
    external_url = models.URLField(
        blank=True, null=True, help_text="External URL (optional, used if no page is selected)"
    )
    order = models.IntegerField(default=0, help_text="Lower numbers appear first")
    is_active = models.BooleanField(default=True, help_text="Show this item in navigation")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.parent and self.parent.parent:
            raise ValueError("Navigation items can only be nested 1 level deep")
        super().save(*args, **kwargs)

    def get_url(self):
        """Returns the URL for this nav item"""
        if self.page:
            return self.page.get_absolute_url()
        if self.external_url:
            return self.external_url
        return "#"

    def has_children(self):
        """Check if this nav item has any active children"""
        return self.children.filter(is_active=True).exists()

    def is_top_level(self):
        """Check if this is a top-level navigation item"""
        return self.parent is None

    def __str__(self):
        if self.parent:
            return f"{self.parent.title} > {self.title}"
        return self.title

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Navigation Item"
        verbose_name_plural = "Navigation Items"
