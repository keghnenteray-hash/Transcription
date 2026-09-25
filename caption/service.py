from faster_whisper import WhisperModel

model = WhisperModel('base', device='cpu', compute_type='int8')

def transcribe_to_srt(file_path):
    segments, info = model.transcribe(
        file_path,
        word_timestamps=True
    )
    
    srt_content = ""
    
    for index, segment in enumerate(segments, start=1):
        start = format_timestamp(segment.start)
        end = format_timestamp(segment.end)
        
        srt_content += (
            f"{index}\n"
            f"{start} --> {end}\n"
            f"{segment.text.strip()}\n\n"
        )
        
    return srt_content
        
            
def format_timestamp(second: float) -> str:
   hrs = int(second / 3600)
   mins = int((second % 3600) / 60)
   secs = int(second % 60)
   msec = int(round((second % 1) *1000))

   return f"{hrs:02}:{mins:02}:{secs:02},{msec:03}"