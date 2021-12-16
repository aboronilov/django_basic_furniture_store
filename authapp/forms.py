from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from django.forms import HiddenInput, forms


class ShopUserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form control {field_name}'


class AgeValidatorMixIn:
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and age < 18:
            raise forms.ValidationError('Вы слишком молоды')
        return age


class ShopUserCreationForm(AgeValidatorMixIn, UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "password1", "password2", "email", "age")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form control {field_name}'
            field.help_text = ''

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and age < 18:
            raise forms.ValidationError('Вы слишком молоды')
        return age


class ShopUserChangeForm(AgeValidatorMixIn, UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "password", "first_name", "last_name", "age", "avatar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = HiddenInput()
                continue
            field.widget.attrs['class'] = f'form control {field_name}'
            field.help_text = ''


