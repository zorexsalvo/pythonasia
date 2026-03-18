def announcement_context(request):
    """Inject latest published announcement and active navbar CTAs into template context."""
    from app.announcements.models import Announcement, ButtonCTA, RibbonCTA

    return {
        "latest_announcement": Announcement.get_latest_published(),
        "ribbon_cta": RibbonCTA.get_active(),
        "button_cta": ButtonCTA.get_active(),
    }
