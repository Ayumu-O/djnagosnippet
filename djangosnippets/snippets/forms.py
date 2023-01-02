from django import forms

from snippets.models import Snippet, Comment, Tag

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ('title', 'tags', 'lang', 'code', 'description')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows':2})
        }
