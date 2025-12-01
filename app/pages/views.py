from django.views.generic import DetailView

from app.pages.models import Page


class PageDetailView(DetailView):
    model = Page
    template_name = "pages/detail.html"
    context_object_name = "page"

    def get_queryset(self):
        return Page.objects.filter(is_published=True)
