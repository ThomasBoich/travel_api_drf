from django import forms
from travels.models import Travel, Country


class TravelersForm(forms.ModelForm):
    country = forms.ModelMultipleChoiceField(queryset=Country.objects.all(), required=False)

    class Meta:
        model = Travel
        fields = '__all__'
        exclude = ['user', 'tipr_users']  # Exclude the 'user' field from the form

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TravelersForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(TravelersForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
            self.save_m2m()  # Save the many-to-many relationships
        return instance