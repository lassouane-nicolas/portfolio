from django.db import models
from django.forms import CheckboxSelectMultiple

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, FieldRowPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    intro = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Introduction",
    )

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

class StandardPage(Page):
    body = RichTextField(
        blank=True,
        verbose_name="Contenu",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

class AboutPage(Page):
    body = RichTextField(
        blank=True,
        verbose_name="Contenu",
    )
    approach = RichTextField(
        blank=True,
        verbose_name="Ma démarche",
    )
    about_technologies = ParentalManyToManyField(
        "home.Technology",
        blank=True,
        related_name="about_pages",
        verbose_name="Technologies maîtrisées",
    )
    timeline_before = models.TextField(
        blank=True,
        verbose_name="Parcours - Avant",
    )
    timeline_transition = models.TextField(
        blank=True,
        verbose_name="Parcours - La transition",
    )
    timeline_today = models.TextField(
        blank=True,
        verbose_name="Parcours - Aujourd'hui",
    )

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("approach"),
        FieldPanel("timeline_before"),
        FieldPanel("timeline_transition"),
        FieldPanel("timeline_today"),
        FieldPanel(
            "about_technologies",
            widget=CheckboxSelectMultiple,
        ),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        technologies = self.about_technologies.all()

        context["technology_groups"] = [
            {
                "title": label,
                "technologies": [
                    technology
                    for technology in technologies
                    if technology.category == value
                ],
            }
            for value, label in Technology.Category.choices
        ]

        return context

class ProjectIndexPage(Page):
    intro = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Introduction",
    )

    parent_page_types = ["home.HomePage"]
    subpage_types = ["home.ProjectPage"]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["projects"] = ProjectPage.objects.child_of(self).live()

        return context

@register_snippet
class Technology(models.Model):
    class Category(models.TextChoices):
        DEVELOPMENT = "development", "Développement"
        DATA = "data", "Données"
        TOOLS = "tools", "Outils & méthodes"

    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Nom",
    )
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.DEVELOPMENT,
        verbose_name="Catégorie",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("category"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Technologie"
        verbose_name_plural = "Technologies"
        ordering = ["name"]

class ProjectPage(Page):
    summary = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Résumé",
    )
    body = RichTextField(
        blank=True,
        verbose_name="Description",
    )
    technologies = models.CharField(
        max_length=250,
        blank=True,
        verbose_name="Technologies",
    )
    project_technologies = ParentalManyToManyField(
        "home.Technology",
        blank=True,
        related_name="projects",
        verbose_name="Technologies associées",
    )
    repository_url = models.URLField(
        blank=True,
        verbose_name="Dépôt GitHub",
    )
    demo_url = models.URLField(
        blank=True,
        verbose_name="Démonstration",
    )

    parent_page_types = ["home.ProjectIndexPage"]
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel("summary"),
        FieldPanel("body"),
        FieldPanel("technologies"),
        FieldPanel(
            "project_technologies",
            widget=CheckboxSelectMultiple,
        ),
        FieldPanel("repository_url"),
        FieldPanel("demo_url"),
    ]

class ContactFormField(AbstractFormField):
    page = ParentalKey(
        "home.ContactPage",
        on_delete=models.PROTECT,
        related_name="form_fields",
    )

    panels = [
        FieldPanel("label"),
        FieldPanel("field_type"),
        FieldPanel("required"),
        FieldPanel("help_text"),
    ]

class ContactPage(AbstractEmailForm):
    intro = models.TextField(
        blank=True,
        verbose_name="Introduction",
    )
    thank_you_text = RichTextField(
        blank=True,
        verbose_name="Message de confirmation",
    )

    parent_page_types = ["home.HomePage"]
    subpage_types = []

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Champs du formulaire"),
        FieldPanel("thank_you_text"),
        FieldPanel("to_address"),
        FieldPanel("from_address"),
        FieldPanel("subject"),
    ]
