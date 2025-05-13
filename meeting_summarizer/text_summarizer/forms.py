from django import forms

class UploadTextForm(forms.Form):
    text_file = forms.FileField(label="Select a .txt file", required=True)
    text_file.widget.attrs.update({'accept': '.txt'})

    def clean_text_file(self):
        text_file = self.cleaned_data['text_file']
        if not text_file.name.endswith('.txt'):
            raise forms.ValidationError("Please upload a .txt file.")
        # You might want to add more file size or type validation here
        return text_file