from django import forms
from .models import Post, Category, Comment


choices = Category.objects.all().values_list('name','name')

choice_list = []

for choice in choices:
    choice_list.append(choice)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author','category', 'body', 'snippet','publish','status', 'header_image')


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug' : forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value' : "", "id" : "elder", 'type':'hidden' }),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet' : forms.TextInput(attrs={'class': 'form-control'}),
            'publish': forms.TextInput(attrs={'class': 'form-control'}),
            # 'created': forms.TextInput(attrs={'class': 'form-control'}),
            # 'updated': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            } 
    
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'snippet')


        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'slug' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            # 'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet' : forms.TextInput(attrs={'class': 'form-control'})
            # 'publish': forms.TextInput(attrs={'class': 'form-control'}),
            # 'created': forms.TextInput(attrs={'class': 'form-control'}),
            # 'updated': forms.TextInput(attrs={'class': 'form-control'}),
            # 'status': forms.Select(attrs={'class': 'form-control'}),
            } 
        

class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'body': forms.Textarea(attrs={'class': 'form-control'}), }
     
