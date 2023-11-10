# import form
# forms.py
from django import forms
from django.shortcuts import get_object_or_404

from .models import Fields
from django import forms
from django.contrib.auth.forms import UserCreationForm  # built in forms for user creation
from .models import Add_comment


class FillInForms(forms.ModelForm):
    class Meta:
        model = Fields
        fields = ('title', 'author','authorHidden', 'updated_on', 'content', 'created_on', 'image', 'video')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # JS will automalically looks for value id
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'authorHidden': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'name', 'type':'hidden'}),
            'updated_on': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'created_on': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

        def get_object(self, queryset=None):
            title_id = self.kwargs.get('title_id')
            return get_object_or_404(Fields, pk=title_id)


# for edit in view
class EditForms(forms.ModelForm):
    class Meta:
        model = Fields
        fields = ('title', 'updated_on', 'content', 'image', 'video')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'This is Title place holder.'}),
            'updated_on': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Add_comment
        fields = ('name','body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }
