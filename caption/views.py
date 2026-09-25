from django.shortcuts import render
from django.http import HttpResponse
from faster_whisper import WhisperModel
from . forms import TranscriptionForm
from . service import transcribe_to_srt

# Create your views here.

def transcribe_file(request):
    form = TranscriptionForm(request.POST, request.FILES)

    if form.is_valid():
        uploaded_file = form.cleaned_data["media_file"]
        
        file_path = f"/tmp/{uploaded_file.name}"
        
        with open(file_path, "wb+") as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)
                
        srt_content = transcribe_to_srt(file_path)
        
        response = HttpResponse(
            srt_content,
            content_type="application/x-subrip"
        )
        
        response["Content-Disposition"] = (
            'attachment; filename="transcription.srt"'
        )
        
        return response
    else:
        form = TranscriptionForm()
        
    return render(request, "index.html", {'form':form})

