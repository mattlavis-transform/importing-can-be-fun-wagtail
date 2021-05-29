from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField
from rest_framework.fields import Field

from wagtail.api import APIField

    
class HeadingContainer(Page):
    search_fields = Page.search_fields + []
    content_panels = Page.content_panels + []
    api_fields = []
    
    subpage_types = [
        'heading.Heading',  # appname.ModelName
    ]

    
class Heading(Page):
    body = MarkdownField(blank=True)
    priority = models.IntegerField(blank=True)
    link_text = models.CharField(max_length=255, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('priority', classname="full"),
        FieldPanel('link_text', classname="full"),
        FieldPanel('body', classname="full"),
    ]
    
    api_fields = [
        APIField('priority'),
        APIField('body'),
        APIField('link_text'),
    ]
    
    subpage_types = []
    
    class Meta:
        verbose_name = "Results page subsection (or header)"
        verbose_name_plural = "Results page subsections"

    
class SuperHeadingContainer(Page):
    search_fields = Page.search_fields + []
    content_panels = Page.content_panels + []
    api_fields = []
    
    subpage_types = [
        'heading.SuperHeading',  # appname.ModelName
    ]

class HeadingSerializer(Field):
    def to_representation(self, child_pages):
        headings = []
        for child in child_pages:
            child_dict = {
                'id': child.id,
            }
            headings.append(child_dict)
        return headings
    
class SuperHeading(Page):
    body = MarkdownField(blank=True)
    priority = models.CharField(max_length=2, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('priority', classname="full"),
        FieldPanel('body', classname="full"),
    ]
    
    api_fields = [
        APIField('priority'),
        APIField('body'),
        APIField('headings', serializer=HeadingSerializer(source="get_child_pages")),
    ]
    
    @property
    def get_child_pages(self):
        return self.get_children().public().live() # .values("id", "slug", "title")

    subpage_types = [
        'heading.Heading',  # appname.ModelName
    ]
