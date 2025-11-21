from collections import defaultdict
from typing import Any

from bakery.views import BuildableTemplateView

from app.speakers.models import Speaker
from app.sponsors.models import Sponsor
from config.constants import SPONSOR_TYPE_ORDER


class HomeView(BuildableTemplateView):
    template_name = "home/index.html"
    build_path = "index.html"

    def get_sponsors(self):
        sponsors_by_type = defaultdict[Any, list](list)
        for sponsor in Sponsor.objects.all():
            sponsors_by_type[sponsor.sponsor_type].append(sponsor)

        return {
            sponsor_type: sponsors_by_type.get(sponsor_type, [])
            for sponsor_type in SPONSOR_TYPE_ORDER
            if sponsor_type in sponsors_by_type
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sponsors_by_type"] = self.get_sponsors()
        context["featured_speakers"] = Speaker.objects.filter(is_featured=True).order_by("first_name", "last_name")
        context["speakers"] = Speaker.objects.filter(is_featured=False).order_by("first_name", "last_name")
        return context


class InternalPageView(BuildableTemplateView):
    """Base view for internal pages with consistent template structure"""

    template_name = "internal/index.html"
    page_template = None  # Override in subclasses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_template"] = self.page_template
        return context


class CodeOfConductView(InternalPageView):
    build_path = "code-of-conduct/index.html"
    page_template = "internal/pages/code-of-conduct.html"


class PartnershipView(InternalPageView):
    build_path = "partnership/index.html"
    page_template = "internal/pages/partnership.html"


class TravelInfoView(InternalPageView):
    build_path = "travel-info/index.html"
    page_template = "internal/pages/travel-info.html"


class AidScholarshipsView(InternalPageView):
    build_path = "aid-scholarships/index.html"
    page_template = "internal/pages/aid-scholarships.html"


class CovidPolicyView(InternalPageView):
    build_path = "covid-policy/index.html"
    page_template = "internal/pages/covid-policy.html"


class DataPrivacyView(InternalPageView):
    build_path = "data-privacy/index.html"
    page_template = "internal/pages/data-privacy.html"


class EveryoneWhoCanPaysView(InternalPageView):
    build_path = "everyone-who-can-pays/index.html"
    page_template = "internal/pages/everyone-who-can-pays.html"


class PatronAcknowledgmentView(InternalPageView):
    build_path = "patron-acknowledgment/index.html"
    page_template = "internal/pages/patron-acknowledgment.html"


class ScheduleView(InternalPageView):
    build_path = "schedule/index.html"
    page_template = "internal/pages/schedule.html"


class VolunteersView(InternalPageView):
    build_path = "volunteers/index.html"
    page_template = "internal/pages/volunteers.html"
