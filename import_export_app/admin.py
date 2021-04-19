from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from import_export.fields import Field
from .models import Document, DocumentField
from import_export import resources, fields, widgets
from django.dispatch import receiver
from import_export.signals import post_import, post_export


# Register your models here.


class DocumentResources(resources.ModelResource):
    # date_expired = Field(attribute='date_expired', column_name='date_testing')
    # myfield = Field(column_name='myfield')
    # full_title = Field()
    delete = fields.Field(widget=widgets.BooleanWidget())

    def for_delete(self, row, instance):
        return self.fields['delete'].clean(row)

    class Meta:
        model = Document
        fields = ('id__title__text__user__target__date_expired')

        @receiver(post_import, dispatch_uid='balabala...')
        def _post_import(model, **kwargs):
            pass

        @receiver(post_export, dispatch_uid='balabala...')
        def _post_export(model, **kwargs):
            pass

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


class DocumentAdmin(ImportExportActionModelAdmin):
    list_display = ['title', 'text', 'date', 'user', 'target', 'date_expired']


admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentField)
