from django.shortcuts import render
from .forms import UploadTextForm
# from .models import UploadedText # If you're using the model
# from .utils import summarize_text # Your summarization logic

def upload_text(request):
    if request.method == 'POST':
        form = UploadTextForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['text_file']
            try:
                text_content = uploaded_file.read().decode('utf-8')
                summary = summarize_text(text_content)
                return render(request, 'text_summarizer/summary.html', {'summary': summary})
            except UnicodeDecodeError:
                form.add_error('text_file', "Could not decode the uploaded file as UTF-8 text.")
    else:
        form = UploadTextForm()
    return render(request, 'text_summarizer/upload_form.html', {'form': form})

# Placeholder for your summarization logic
def summarize_text(text):
    return f"This is a placeholder summary of the text from: {text[:50]}..."