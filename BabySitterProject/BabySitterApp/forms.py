from django import forms

from .models import babySitter

class babySitterForm(forms.ModelForm):
    class Meta:
        model = babySitter
        fields = "__all__"