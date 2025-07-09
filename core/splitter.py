import os, subprocess
from cli.styles import console

def audio_split(input_file: str, output_dir: str, concert):
    for i, track in enumerate(concert.tracks):
        start_time = track.start
        end_time = concert.tracks[i + 1].start if i + 1 < len(concert.tracks) else concert.duration
        output_file = os.path.join(output_dir, f"{i}. {track.title}.mp3")

        command = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel", "error",
            "-ss", start_time,
            "-to", end_time,
            "-i", input_file,
            "-map", "0:a",
            "-c", "copy",
            "-id3v2_version", "3",
            output_file
        ]

        try:
            subprocess.run(command, check=True)
            console.print(f"\t[important]Split and saved track:[/important] [important_bold]{track.title}[/important_bold]. [important]start: {start_time}, end: {end_time}[/important]")
        except subprocess.CalledProcessError as e:
            print(f"[error_title]Error splitting track {track.title}:[/error_title] [error_message]{e}[/error_message]")