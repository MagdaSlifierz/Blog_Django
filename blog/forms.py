from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('name','name')

choice_list = []

for choice in choices:
    choice_list.append(choice)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author','category', 'body', 'publish','status')


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug' : forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value' : "", "id" : "elder", 'type':'hidden' }),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'publish': forms.TextInput(attrs={'class': 'form-control'}),
            # 'created': forms.TextInput(attrs={'class': 'form-control'}),
            # 'updated': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            } 
    
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'slug' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            # 'publish': forms.TextInput(attrs={'class': 'form-control'}),
            # 'created': forms.TextInput(attrs={'class': 'form-control'}),
            # 'updated': forms.TextInput(attrs={'class': 'form-control'}),
            # 'status': forms.Select(attrs={'class': 'form-control'}),
            } 