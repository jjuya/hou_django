from django import forms

from .models import *

class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ('title', )

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ('title', )
