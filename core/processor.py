from core import downloader, audio_extractor, splitter, tagger
from cli.styles import console
import os

def pipeline(concert):
    
    if (concert.source_type == 'youtube'):
        try:
            # Download the audio from YouTube as an MP4 file
            print(f"Downloading audio from YouTube: {concert.video_url}")
            downloader.download_audio(concert, 'concert_audio.mp4')
            print("Downloaded successfully.")
        except Exception as e:
            # If there's an error downloading, print it and exit
            print(f"Error downloading audio from YouTube: {e}")
            exit(1)
        try:
            # Convert the downloaded MP4 file to MP3
            print("Converting the audio.")
            audio_extractor.convert_audio('concert_audio.mp4', 'audio.mp3')
            full_audio_path = 'audio.mp3'  # This is the converted MP3 file path
            # Remove the original MP4 file after conversion
            os.remove('concert_audio.mp4') 

        except Exception as e:
            # If there's an error converting the audio, print it and exit
            print(f"Error converting audio: {e}")
            exit(1)
        
    # Case where the source is a local file
    else:
        print("Local audio source detected. No download needed.")
        # If the local file is already in MP3 format, no conversion is needed
        if str(concert.file_source).endswith('.mp3'):
            print("Local audio file is in MP3 format. No conversion needed.")
            full_audio_path = str(concert.file_source)
        else:
            try:
                # If the local file is not in MP3 format, convert it to MP3
                print(f"Converting local audio file {concert.file_source} to MP3.")
                audio_extractor.convert_audio(str(concert.file_source), 'audio.mp3')
                full_audio_path = 'audio.mp3'  # This is the converted MP3 file path
            except Exception as e:
                # If there's an error during conversion, print it and exit
                print(f"Error converting local audio file to mp3: {e}")
                exit(1)

    # Attempt to split the audio file into smaller segments
    try:
        print(f"Splitting audio file into segments.")
        splitter.audio_split(full_audio_path, './temp', concert)
        print("Audio split successfully. Proceeding to tagging.")
        # Remove the original MP3 file after splitting, if it was converted from local file
        os.remove(full_audio_path)  if not str(concert.file_source).endswith('.mp3') else None
    except Exception as e:
        # If there's an error splitting the audio, print it, clean up temp files, and exit
        print(f"Error splitting audio: {e}")
        for file in os.listdir('./temp'):
            os.remove(os.path.join('./temp', file))  # Remove any temp files that were created
        exit(1)

    # Attempt to add metadata to the split audio files
    try:
        print("Adding metadata to the split audio files.")
        tagger.add_metadata('./temp', concert.output_dir, concert)
        print("Metadata added successfully.")
        # Clean up the temp folder by removing any files after adding metadata
        for file in os.listdir('./temp'):
            os.remove(os.path.join('./temp', file))

    except Exception as e:
        # If there's an error adding metadata, print it and exit
        print(f"Error adding metadata: {e}")
        exit(1)
