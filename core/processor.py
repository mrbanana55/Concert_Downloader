from pytubefix import YouTube
from config_loader import load_concert
import os, ffmpeg, subprocess


def download_audio(concert, output_name):    
    video_url = YouTube(str(concert.video_url))
    audio_stream = video_url.streams.filter(only_audio=True).order_by('abr').desc().first()
    audio_stream.download(filename=output_name)


#Convert the audio to the desired format
def convert_audio(input_file: str, output_file: str):
    command = [
        "ffmpeg",
        "-i", input_file,
        output_file
    ]
    try:
        subprocess.run(command, check=True)
        print(f"Converted {input_file} to {output_file}")

    except ffmpeg.Error as e:
        print(f"Error converting audio: {e}")



def audio_split(input_file: str, output_dir: str, concert):
    for i, track in enumerate(concert.tracks):
        start_time = track.start
        end_time = track.end
        output_file = os.path.join(output_dir, f"{i}. {track.title}.mp3")

        command = [
            "ffmpeg",
            "-ss", start_time,
            "-i", input_file,
            "-to", end_time,
            "-map", "0:a",
            "-c", "copy",
            "-id3v2_version", "3",
            output_file
        ]

        try:
            subprocess.run(command, check=True)
            print(f"Split and saved track: {track.title}")
        except subprocess.CalledProcessError as e:
            print(f"Error splitting track {track.title}: {e}")

def add_metadata(input_dir: str, output_dir: str, concert):
    for track in concert.tracks:
        input_file = os.path.join(input_dir, f"{track.number - 1}. {track.title}.mp3")
        output_file = os.path.join(output_dir, f"{track.title}.mp3")

        command = [
            "ffmpeg",
            "-i", input_file,
            "-i", concert.cover_image,
            "-map", "0:a",
            "-map", "1:v",
            "-c", "copy",
            "-metadata", f"title={track.title}",
            "-metadata", f"track={track.number}",
            "-metadata", f"artist={concert.artist}",
            "-metadata", f"album={concert.album}",
            "-id3v2_version", "3",
            output_file
            ]
        try:
            subprocess.run(command, check=True)
            print(f"Added metadata to track: {track.title}")
        except subprocess.CalledProcessError as e:
            print(f"Error adding metadata to track {track.title}: {e}")



#TEST VARIABLES
concert = load_concert('config.json')
download_audio(concert, 'concert_audio.mp4')
convert_audio('concert_audio.mp4', 'audio.mp3')
audio_split('audio.mp3', 'C:/Users/dlega/Desktop/Concert_Downloader/temp', concert)
add_metadata('C:/Users/dlega/Desktop/Concert_Downloader/temp', 'C:/Users/dlega/Desktop/Concert_Downloader/output', concert)