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

class BookmarkForm(forms.ModelForm):

    class Meta:
        model = Bookmark
        fields = ('title', 'url', 'list')
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'url' : forms.TextInput(attrs={'class' : 'form-control'}),
            'list' : forms.Select(attrs={'class' : 'form-control'})
        }
