from core import downloader, audio_extractor, splitter, tagger
from cli.styles import console
import os

def pipeline(concert):
    
    if (concert.source_type == 'youtube'):
        try:
            # Download the audio from YouTube as an MP4 file
            with console.status(f"\t[progress_message]Downloading audio from YouTube: {concert.video_url} ...[/progress_message]"):
                downloader.download_audio(concert, 'concert_audio.mp4')
        except Exception as e:
            # If there's an error downloading, print it and exit
            print(f"\t[error_title]Error downloading audio from YouTube:[/error_title] [error_message]{e}[/error_message]")
            exit(1)
        try:
            # Convert the downloaded MP4 file to MP3
            with console.status("\t[progress_message]Converting the audio.[/progress_message]"):
                audio_extractor.convert_audio('concert_audio.mp4', 'audio.mp3')
                full_audio_path = 'audio.mp3'  # This is the converted MP3 file path
            # Remove the original MP4 file after conversion
            os.remove('concert_audio.mp4') 

        except Exception as e:
            # If there's an error converting the audio, print it and exit
            print(f"[error_title]Error converting audio:[/error_title] [error_message]{e}[/error_message]")
            exit(1)
        
    # Case where the source is a local file
    else:
        console.print("\t[important]Local audio source detected. No download needed.[/important]")
        # If the local file is already in MP3 format, no conversion is needed
        if str(concert.file_source).endswith('.mp3'):
            console.print("\t[important]Local audio file is in MP3 format. No conversion needed.[/important]")
            full_audio_path = str(concert.file_source)
        else:
            try:
                # If the local file is not in MP3 format, convert it to MP3
                with console.status(f"\t[progress_message]Converting local audio file[/progress_message] [progress_title]{concert.file_source}[/progress_title] [progress_message]to MP3.[/progress_message]"):
                    audio_extractor.convert_audio(str(concert.file_source), 'audio.mp3')
                    full_audio_path = 'audio.mp3'  # This is the converted MP3 file path
            except Exception as e:
                # If there's an error during conversion, print it and exit
                console.print(f"\t[error_title]Error converting local audio file to mp3:[/error_title] [error_message]{e}[/error_message]")
                exit(1)
    # Attempt to split the audio file into smaller segments
    try:
        with console.status(f"\t[progress_message]Splitting audio file into segments.[/progress_message]"):
            splitter.audio_split(full_audio_path, './temp', concert)
            console.print("\t[important]Audio split successfully. Proceeding to tagging.[/important]")
        # Remove the original MP3 file after splitting, if it was converted from local file
        os.remove(full_audio_path)  if not str(concert.file_source).endswith('.mp3') else None
    except Exception as e:
        # If there's an error splitting the audio, print it, clean up temp files, and exit
        console.print(f"[error_title]Error splitting audio:[/error_title] [error_message]{e}[/error_message]")
        for file in os.listdir('./temp'):
            os.remove(os.path.join('./temp', file))  # Remove any temp files that were created
        exit(1)
    # Attempt to add metadata to the split audio files
    try:
        with console.status("\t[progress_message]Adding metadata to the split audio files.[/progress_message]"):
            tagger.add_metadata('./temp', concert.output_dir, concert)
            console.print("\t[important]Metadata added successfully.[/important]")
            # Clean up the temp folder by removing any files after adding metadata
            for file in os.listdir('./temp'):
                os.remove(os.path.join('./temp', file))

    except Exception as e:
        # If there's an error adding metadata, print it and exit
        console.print(f"[error_title]Error adding metadata:[/error_title] [error_message]{e}[/error_message]")
        exit(1)
