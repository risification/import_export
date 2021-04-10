from django.contrib import admin
from import_export.fields import Field
from .models import Document
from import_export import resources


# Register your models here.


class DocumentResources(resources.ModelResource):
    # date_expired = Field(attribute='date_expired', column_name='date_testing')
    # myfield = Field(column_name='myfield')
    full_title = Field()

    class Meta:
        model = Document
        fields = ('id__title__text__user')
        '''widjets = {
            'date': {'format': '%d.%m.%Y'}
        }'''
        # skip_unchanged = True
        # report_skipped = False
        # import_id_fields = ('isbn',)
        # exclude = ('imported')
        # export_order = ('id', 'user', 'date', 'text', 'title' )

    '''def dehydrate_full_title(self, document):
        return '%s by %s' % (document.title, document.text)'''


admin.site.register(Document)
