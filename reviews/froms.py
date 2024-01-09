from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget.attrs.update({
            'class': 'appearance-none bg-white border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none',
            'placeholder': 'Your comment...',
            'aria-label': 'Comment',
        })