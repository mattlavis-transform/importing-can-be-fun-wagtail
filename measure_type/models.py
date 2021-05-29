from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index
from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField

    
class MeasureTypeContainer(Page):
    search_fields = Page.search_fields + []
    content_panels = Page.content_panels + []
    api_fields = []
    
    subpage_types = [
        'measure_type.MeasureType',  # appname.ModelName
    ]
    
class MeasureType(Page):
    measure_type = models.CharField(max_length=3, blank=True)
    overlay = MarkdownField(blank=True)


    search_fields = Page.search_fields + [
        index.SearchField('measure_type'),
        index.SearchField('overlay'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('measure_type', classname="full"),
        FieldPanel('overlay', classname="full"),
    ]
    
    subpage_types = []
