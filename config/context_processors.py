def announcement_context(request):
    """Inject latest published announcement and active ribbon CTA into template context."""
    from app.announcements.models import Announcement, RibbonCTA

    return {
        "latest_announcement": Announcement.get_latest_published(),
        "ribbon_cta": RibbonCTA.get_active(),
    }
