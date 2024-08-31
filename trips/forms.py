from django import forms
from .models import Trip


class TravelersForm(forms.ModelForm):
    #country = forms.ModelMultipleChoiceField(queryset=Country.objects.all(), required=False)

    class Meta:
        model = Trip
        fields = '__all__'
        exclude = ['user', 'trip_users','tipr_users','trip_date','free_seats','city','price','status','finish','cityin','trip_in_time','trip_out_time','trip_car','trip_baggage','trip_smoking','trip_hild_seat','trip_animals',]  # Exclude the 'user' field from the form
        


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