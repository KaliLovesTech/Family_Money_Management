from django import forms
from django.contrib.auth.models import User
from .models import Profile
from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('first_name', css_class='form-control'),
            Field('last_name', css_class='form-control'),
            Field('email', css_class='form-control'),
        )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'bio', 'birth_date', 'profile_picture', 'phone_number', 'address']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('bio', css_class='form-control'),
            Field('location', css_class='form-control'),
            Field('birth_date', css_class='form-control'),
            Field('phone_number', css_class='form-control'),
            Field('address', css_class='form-control'),
            Field('profile_picture', css_class='form-control'),
        )

class CustomSignupForm(SignupForm):
    bio = forms.CharField(max_length=500, required=False, label='Bio', widget=forms.Textarea(attrs={'rows': 3}))
    location = forms.CharField(max_length=100, required=False, label='Location')

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('username', css_class='form-control'),
            Field('email', css_class='form-control'),
            Field('password1', css_class='form-control'),
            Field('password2', css_class='form-control'),
            Field('bio', css_class='form-control'),
            Field('location', css_class='form-control'),
            Submit('submit', 'Sign Up', css_class='btn btn-primary'),
        )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.profile.bio = self.cleaned_data.get('bio')
        user.profile.location = self.cleaned_data.get('location')
        user.profile.save()
        return user