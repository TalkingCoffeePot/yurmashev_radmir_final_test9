from accounts.models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class NewUserForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = [
            'username', 'password1', 'password2',
            'first_name', 'avatar', 'email', 
            'info', 'number', 'sex'
        ]
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder': 'Логин', 'class': 'input_box'}),
            'first_name' : forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'input_box'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'Электронная почта', 'class': 'input_box'}),
            'info' : forms.Textarea(attrs={'placeholder': 'О себе', 'class': 'input_box text_box'}),
            'number' : forms.NumberInput(attrs={'placeholder': 'Номер телефона', 'class': 'input_box'}),
            'sex' : forms.RadioSelect(attrs={'placeholder': 'Пол', 'class': 'input_box d-flex flex-row justify-content-around'}),
        }
        
    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) < 1:
            raise forms.ValidationError("Email обязателен к заполнению!")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        if len(cleaned_data['first_name']) < 1:
            raise forms.ValidationError("Хотя бы одно поле ИМЕНИ должно быть заполнено")
        return cleaned_data
    
class UserEditForm(UserChangeForm):
    class Meta:
        model= Profile
        fields = [
            'first_name', 'avatar', 'email', 
            'info', 'number', 'sex'
        ]
        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'input_box'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'Электронная почта', 'class': 'input_box'}),
            'info' : forms.Textarea(attrs={'placeholder': 'О себе', 'class': 'input_box text_box'}),
            'number' : forms.NumberInput(attrs={'placeholder': 'Номер телефона', 'class': 'input_box'}),
            'sex' : forms.RadioSelect(attrs={'placeholder': 'Пол', 'class': 'input_box d-flex flex-row justify-content-around'}),
        }

        