from pytubefix import YouTube
from cli.styles import console

def download_audio(concert, output_name):
    try:    
        video_url = YouTube(str(concert.video_url))
    except Exception as e:
        console.print(f"[error_title]Error fetching YouTube video:[/error_title] [error_message]{e}.\n Please check the URL or your internet connection.[/error_message]")
        return
    audio_stream = video_url.streams.filter(only_audio=True).order_by('abr').desc().first()
    audio_stream.download(filename=output_name)