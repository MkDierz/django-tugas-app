# import form class from django
from django import forms

# import GeeksModel from models.py
from .models import MataKuliah, Tugas
import datetime
from django.forms import ModelChoiceField


class MatkuliahFormChoices(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nama


# create a ModelForm
class MatkuliahForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = MataKuliah
        fields = "__all__"


class TugasForm(forms.ModelForm):
    matakuliah = MatkuliahFormChoices(queryset=MataKuliah.objects.all())

    class Meta:
        model = Tugas
        fields = "__all__"
        widgets = {
            'kumpul': forms.TextInput(
                attrs={'class': 'form-control fc-datepicker',
                       "placeholder": "MM/DD/YYYY"}),
        }
