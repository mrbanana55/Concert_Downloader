import yt_dlp
import logging

logger = logging.getLogger(__name__)

def download_audio(concert, output_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_name,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        'quiet': True,
        'no_warnings': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([str(concert.video_url)])
    except Exception as e:
        logger.error(f"Error fetching YouTube video: {e}.\n Please check the URL or your internet connection.")