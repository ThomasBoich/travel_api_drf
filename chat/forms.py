from django import forms

class MessageForm(forms.Form):
    recipient_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    message_content = forms.CharField(widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        initial['recipient_id'] = kwargs.get('recipient_id')
        kwargs['initial'] = initial
        super(MessageForm, self).__init__(*args, **kwargs)
    

from .models import Folder

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'dialogs']
        widgets = {
            'dialogs': forms.CheckboxSelectMultiple
        }