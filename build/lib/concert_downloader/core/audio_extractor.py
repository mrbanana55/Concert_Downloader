import subprocess, ffmpeg, logging

logger = logging.getLogger(__name__)

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
        logger.info(f"Converted {input_file} to {output_file}")

    except ffmpeg.Error as e:
        logger.error(f"Error converting audio: {e}")
