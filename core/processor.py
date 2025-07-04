from config_loader import load_concert
from core import downloader, audio_extractor, splitter, tagger
import os

#Pending: Verify all folders exist, if not create them
#Pending: What if it's a youtube source

try:
    concert = load_concert('example.json')
except Exception as e:
    print(f"Error loading concert configuration: {e}")
    exit(1)

#pending: what if it's a youtube source
if (concert.source_type == 'youtube'):
    downloader.download_audio(concert, 'concert_audio.mp4')
    try:
        audio_extractor.convert_audio('concert_audio.mp4', 'audio.mp3')
    except Exception as e:
        print(f"Error converting audio: {e}")
        exit(1)

#case it's a local file
elif (concert.source_type == 'local'):
    print("Local audio source detected. No download needed.")
    if str(concert.file_source).endswith('.mp3'):
       print("Local audio file is in MP3 format. No conversion needed.")
       full_audio_path = str(concert.file_source)
    else:
        try:
            audio_extractor.convert_audio(str(concert.file_source), 'audio.mp3')
            full_audio_path = 'audio.mp3' #this may cause trouble since it's a relative path
        except Exception as e:
            print(f"Error converting local audio file to mp3: {e}")
            exit(1)
    try:
        splitter.audio_split(full_audio_path, './temp', concert)
        print("Audio split successfully. Proceeding to tagging.")
        os.remove(full_audio_path)  if not str(concert.file_source).endswith('.mp3') else None
    except Exception as e:
        print(f"Error splitting audio: {e}")
        for file in os.listdir('./temp'):
            os.remove(os.path.join('./temp', file))
        exit(1)

    try:
        tagger.add_metadata('./temp', concert.output_dir, concert)
        print("Metadata added successfully.")
        for file in os.listdir('./temp'):
            os.remove(os.path.join('./temp', file))

    except Exception as e:
        print(f"Error adding metadata: {e}")
        exit(1)

else:
    print(f"Unsupported source: {concert.source_type}. Please use 'youtube' or 'local'.")
    exit(1)