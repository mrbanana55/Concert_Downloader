import subprocess, ffmpeg
from cli.styles import console

#Convert the audio to the desired format
def convert_audio(input_file: str, output_file: str):
    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel", "quiet",
        "-i", input_file,
        output_file
    ]
    try:
        subprocess.run(command, check=True)
        console.print(f"\t[important]Converted {input_file} to {output_file}[/important]")

    except ffmpeg.Error as e:
        print(f"[error_title]Error converting audio:[/error_title] [error_message]{e}[/error_message]")