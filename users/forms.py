from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile, Add_comment


# heritate fromuser information form

class SignUpForm(UserCreationForm):
    # Find the field that we want to add in this
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    # Email field so user Email Input

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control is-valid'
        self.fields['email'].widget.attrs['class'] = 'form-control is-valid'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfilePage(UserChangeForm):
    # Find the field that we want to add in this
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    # author = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Email field so user Email Input

    class Meta:
        model = User
        fields = ('username', 'email',)


class PageForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = ('bio', 'picture_profile', 'facebook_url', 'twitter_url', 'instagram_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            # 'picture_profile': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PageForm(forms.ModelForm):
    class Meta:

        model = Profile
        fields = ('bio', 'picture_profile', 'facebook_url', 'twitter_url', 'instagram_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            # 'picture_profile': forms.TextInput(attrs={'class':'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
