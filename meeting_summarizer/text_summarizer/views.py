from django.shortcuts import render
from .forms import UploadTextForm
# from .models import UploadedText # If you're using the model
# from .utils import summarize_text # Your summarization logic
from text_summarizer.services import TextSummarizerService
def upload_text(request):
    if request.method == 'POST':
        form = UploadTextForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['text_file']
            try:
                text_content = uploaded_file.read().decode('utf-8')
                service= TextSummarizerService()
                summary = service.summarize_text(text_content)
                return render(request, 'text_summarizer/summary.html', {'summary': summary})
            except UnicodeDecodeError:
                form.add_error('text_file', "Could not decode the uploaded file as UTF-8 text.")
    else:
        form = UploadTextForm()
    return render(request, 'text_summarizer/upload_form.html', {'form': form})
