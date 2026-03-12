def announcement_context(request):
    """Inject latest published announcement into template context."""
    from app.announcements.models import Announcement

    return {"latest_announcement": Announcement.get_latest_published()}
