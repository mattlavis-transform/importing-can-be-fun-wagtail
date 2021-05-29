from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField
from taggit.models import Tag as TaggitTag
from wagtail.snippets.models import register_snippet
from modelcluster.tags import ClusterTaggableManager
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.api import APIField


class SignpostingStepContainer(Page):
    search_fields = Page.search_fields + []
    content_panels = Page.content_panels + []
    api_fields = []

    subpage_types = [
        'signposting_step.SignpostingStep',  # appname.ModelName
    ]


class SignpostingStep(Page):

    preview_modes = []

    content_trader_declarant = MarkdownField(blank=True)
    content_trader_nondeclarant = MarkdownField(blank=True)
    content_agent = MarkdownField(blank=True)
    priority = models.IntegerField(blank=True)
    sections = models.CharField(blank=True, max_length=1000, verbose_name="Linked to sections")
    chapters = models.CharField(blank=True, max_length=1000, verbose_name="Linked to chapters")

    search_fields = Page.search_fields + [
        index.SearchField('content_trader_declarant'),
        index.SearchField('content_trader_nondeclarant'),
        index.SearchField('content_agent'),
    ]

    tags = ClusterTaggableManager(
        through="signposting_step.SignpostingStepTag", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('content_trader_declarant', classname="full"),
        FieldPanel('content_trader_nondeclarant', classname="full"),
        FieldPanel('content_agent', classname="full"),
        FieldPanel('priority', classname="full"),
        FieldPanel("sections"),
        FieldPanel("chapters"),
        FieldPanel("tags"),
    ]

    api_fields = [
        APIField('content_trader_declarant'),
        APIField('content_trader_nondeclarant'),
        APIField('content_agent'),
        APIField('priority'),
        APIField('sections'),
        APIField('chapters'),
        APIField('tags'),
    ]

class SignpostingStepTag(TaggedItemBase):
    content_object = ParentalKey(
        "SignpostingStep", related_name="signposting_step_tags")

@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
