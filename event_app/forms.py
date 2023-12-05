from django import forms

from .models import Event, ParticipationModel

class EventCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
           
            visible.field.widget.attrs['class'] = 'rounded-md w-full shadow border block my-2'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['organiser']
        widgets = {
            'time': forms.TimeInput(format='%H:%M', attrs={'type': 'time', 'placeholder': 'HH:MM'}),
            'date': forms.TimeInput(attrs={'type': 'date', 'placeholder': '12-03-2001'}),
        }


class ParticipationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
           
            visible.field.widget.attrs['class'] = 'rounded-md w-full shadow border block my-2'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = ParticipationModel
        fields = "__all__"
        exclude = ['event']