from concert_downloader.core import splitter
from concert_downloader.core import tagger
from concert_downloader.errors import ConcertError
import os, logging, tempfile

from concert_downloader.core import audio_extractor, downloader

logger = logging.getLogger(__name__)

def pipeline(concert):
    
    if (concert.source_type == 'youtube'):
        try:
            # Download the audio from YouTube as an MP4 file
            with logger.info(f"Downloading audio from YouTube: {concert.video_url}"):
                downloader.download_audio(concert, 'concert_audio.mp4')
        except Exception as e:
            # If there's an error downloading, print it and exit
            raise ConcertError(f"Error downloading audio from YouTube: {e}") from e
        try:
            # Convert the downloaded MP4 file to MP3
            with logger.info("Converting the audio."):
                audio_extractor.convert_audio('concert_audio.mp4', 'audio.mp3')
                full_audio_path = 'audio.mp3'  # This is the converted MP3 file path
            # Remove the original MP4 file after conversion
            os.remove('concert_audio.mp4') 

        except Exception as e:
            # If there's an error converting the audio, print it and exit
            raise ConcertError(f"Error converting audio: {e}") from e
        
    # Case where the source is a local file
    else:
        logger.info("Local audio source detected. No download needed.")
        # If the local file is already in MP3 format, no conversion is needed
        if str(concert.file_source).endswith('.mp3'):
            logger.info("Local audio file is in MP3 format. No conversion needed.")
            full_audio_path = str(concert.file_source)
        else:
            try:
                # If the local file is not in MP3 format, convert it to MP3
                with logger.info(f"Converting local audio file {concert.file_source} to MP3."):
                    audio_extractor.convert_audio(str(concert.file_source), 'audio.mp3')
                    full_audio_path = 'audio.mp3'  # This is the converted MP3 file path
            except Exception as e:
                # If there's an error during conversion, print it and exit
                raise ConcertError(f"Error converting local audio file to mp3: {e}") from e
            
    # Attempt to split the audio file into smaller segments
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            logger.info(f"Splitting audio file into segments.")
            splitter.audio_split(full_audio_path, temp_dir, concert)
            logger.info("Audio split successfully. Proceeding to tagging.")

            # Remove the original MP3 file after splitting, if it was converted from local file
            os.remove(full_audio_path)  if not str(concert.file_source).endswith('.mp3') else None
        except Exception as e:
            raise ConcertError(f"Error splitting audio: {e}") from e
            
        # Attempt to add metadata to the split audio files
        try:
            with logger.info("Adding metadata to the split audio files."):
                tagger.add_metadata(temp_dir, concert.output_dir, concert)
                logger.info("Metadata added successfully.")
        except Exception as e:
            # If there's an error adding metadata, print it and exit
            raise ConcertError(f"Error adding metadata: {e}") from e
