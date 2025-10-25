from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields= "__all__"
        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your title'
            }),
            "describtion": forms.TextInput(attrs={
                'class': 'form-text',
                'placeholder': 'Enter your description'
            }),
            "image": forms.ClearableFileInput(attrs={
                'class': 'form-input',
            }),
        }
        
                     
                              