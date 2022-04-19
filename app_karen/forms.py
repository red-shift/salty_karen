from django import forms

from .models import KarenPost, Comment


class KarenPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    video = forms.FileField(widget=forms.FileInput(), required=True)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = KarenPost
        fields = ['title', 'name', 'location', 'video', 'description']


class UpdateCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ['content']
