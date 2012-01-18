from bootstrap.forms import BootstrapForm
from django import forms

class FeedbackForm(BootstrapForm):
    message = forms.CharField(label="What's on your heart",
        help_text='Sign with your email address if you want a reply.',
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))
