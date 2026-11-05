from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField


class HomePage(Page):
    intro = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Introduction"
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro")
    ]

class StandardPage(Page):
    body = RichTextField(
        blank=True,
        verbose_name="Contenu"
    )

    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]

class ProjectIndexPage(Page):
    parent_page_types = ["home.HomePage"]
    subpage_types = ["home.ProjectPage"]

    def get_context(self, request):
        context = super().get_context(request)
        context["projects"] = ProjectPage.objects.child_of(self).live()

        return context

class ProjectPage(Page):
    summary = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Résumé"
    )
    body = RichTextField(
        blank=True,
        verbose_name="Description"
    )
    technologies = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Technologies"
    )
    repository_url = models.URLField(
        blank=True,
        verbose_name="Dépôt GitHub"
    )
    demo_url = models.URLField(
        blank=True,
        verbose_name="Démonstration"
    )

    parent_page_types = ["home.ProjectIndexPage"]
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
        FieldPanel("body"),
        FieldPanel("technologies"),
        FieldPanel("repository_url"),
        FieldPanel("demo_url")
    ]

class ContactPage(Page):
    intro = models.TextField(
        blank=True,
        verbose_name="Introduction"
    )

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel("intro")
    ]
