from pytubefix import YouTube
import logging

logger = logging.getLogger(__name__)

def download_audio(concert, output_name):
    try:    
        video_url = YouTube(str(concert.video_url))
    except Exception as e:
        logger.error(f"Error fetching YouTube video:{e}.\n Please check the URL or your internet connection.")
        return
    audio_stream = video_url.streams.filter(only_audio=True).order_by('abr').desc().first()
    audio_stream.download(filename=output_name)