from django import forms

class TranscriptionForm(forms.Form):
    media_file = forms.FileField(
        widget=forms.FileInput(attrs={'accept': 'video/*,audio/*'})
    )