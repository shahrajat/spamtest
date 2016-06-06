from django import forms


class NameForm(forms.Form):
    sender = forms.EmailField()
    subject = forms.CharField(label='', max_length=100)
    message = forms.CharField(widget=forms.Textarea, label='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sender'].widget.attrs.update({
            'placeholder': 'Enter sender\'s Email address',
            'class': 'input-box',
            'style':'height: auto',
            'required':'true',
        })
        self.fields['subject'].widget.attrs.update({
            'placeholder': 'Enter subject here',
            'class': 'input-box',
            'style': 'height: auto',
            'required': 'true',
        })
        self.fields['message'].widget.attrs.update({
            'placeholder': 'Enter Email message here',
            'class': 'input-box',
            'required': 'true',
        })
