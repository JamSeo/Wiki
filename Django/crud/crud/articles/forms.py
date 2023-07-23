from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=16)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if 'django' in title:r
    #         return True
    #     return False