from pytubefix import YouTube
from config_loader import load_concert

#TEST VARIABLES
concert = load_concert('config.json')

def download_audio(concert, output_name):    
    video_url = YouTube(str(concert.video_url))
    audio_stream = video_url.streams.filter(only_audio=True).order_by('abr').desc().first()
    audio_stream.download(filename=output_name)

#Convert the audio to the desired format
import ffmpeg, os

def convert_audio(input_file: str, output_file: str):
    # Ensure input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file {input_file} does not exist!")
        return

    try:
        # Specify the full path to ffmpeg executable
        ffmpeg.input(input_file).output(output_file).run(overwrite_output=True)
        print(f"Converted {input_file} to {output_file}")
        os.remove(input_file)  # Optionally remove the original file after conversion
    except ffmpeg.Error as e:
        print(f"Error converting audio: {e}")

#split the audio into segments
import os, ffmpeg, subprocess


def audio_split(input_file: str, output_dir: str):
    cover_image = concert.cover_image
    artist = concert.artist
    album = concert.album
    for track in concert.tracks:
        start_time = track.start
        end_time = track.end
        output_file = os.path.join(output_dir, f"{track.title}.mp3")

        command = [
            "ffmpeg",
            "-i", input_file,
            "-i", cover_image,
            "-map", "0:a",
            "-map", "1:v",
            "-c", "copy",
            "-id3v2_version", "3",
            "-metadata", f"artist={artist}",
            "-metadata", f"album={album}",
            "-metadata", f"title={track.title}",
            "-metadata", f"track={track.number}",
            "-metadata:s:v", "title=Album cover",
            "-metadata:s:v", "comment=Cover (front)",
            output_file
]

        try:
            subprocess.run(command, check=True)
            print(f"Split audio for {track.title} from {start_time} to {end_time}")

        except subprocess.CalledProcessError as e:
            print("Error during ffmpeg execution:", e)

    os.remove(input_file)




download_audio(concert, 'concert_audio.mp4')
convert_audio('concert_audio.mp4', 'audio.mp3')
audio_split('audio.mp3', 'C:/Users/dlega/Desktop/Concert_Downloader/output')