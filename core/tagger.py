import os, subprocess
from cli.styles import console

def add_metadata(input_dir: str, output_dir: str, concert):
    for track in concert.tracks:
        input_file = os.path.join(input_dir, f"{track.number - 1}. {track.title}.mp3")
        output_file = os.path.join(output_dir, f"{track.title}.mp3")

        command = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel", "quiet",
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
            console.print(f"\t[important]Added metadata to track:[/important] [important_bold]{track.title}[/important_bold]")
        except subprocess.CalledProcessError as e:
            console.print(f"[error_title]Error adding metadata to track {track.title}:[error_title] [error_message]{e}[/error_message]")