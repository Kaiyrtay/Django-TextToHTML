from django.forms import ModelForm, CharField
from ckeditor.widgets import CKEditorWidget
# local
from .models import Editor


class EditorForm(ModelForm):
    body = CharField(widget=CKEditorWidget(), label='')

    class Meta:
        model = Editor
        fields = '__all__'
