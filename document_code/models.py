from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField

from wagtail.api import APIField

    
class DocumentCodeContainer(Page):
    search_fields = Page.search_fields + []
    content_panels = Page.content_panels + []
    api_fields = []
    
    subpage_types = [
        'document_code.DocumentCode',  # appname.ModelName
    ]
    
class DocumentCode(Page):
    document_code = models.CharField(max_length=4, blank=True)
    overlay = MarkdownField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('document_code'),
        index.SearchField('overlay'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('document_code', classname="full"),
        FieldPanel('overlay', classname="full"),
    ]
    
    api_fields = [
        APIField('document_code'),
        APIField('overlay'),
    ]
    
    subpage_types = []
    
    template = "test.html"
    