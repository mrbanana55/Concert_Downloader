import os, subprocess, logging

logger = logging.getLogger(__name__)

def add_metadata(input_dir: str, output_dir: str, concert):
    for track in concert.tracks:
        input_file = os.path.join(input_dir, f"{track.number - 1}. {track.title}.mp3")
        output_file = os.path.join(output_dir, f"{track.title}.mp3")

        command = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel", "quiet",
            "-i", input_file,
        ]

        if concert.cover_image:
            command.extend(["-i", str(concert.cover_image)])

        command.extend(["-map", "0:a"])

        if concert.cover_image:
            command.extend(["-map", "1:v"])

        command.extend([
            "-c", "copy",
            "-metadata", f"title={track.title}",
            "-metadata", f"track={track.number}",
        ])

        if concert.artist:
            command.extend(["-metadata", f"artist={concert.artist}"])

        if concert.album:
            command.extend(["-metadata", f"album={concert.album}"])

        command.extend([
            "-id3v2_version", "3",
            output_file
        ])
        try:
            subprocess.run(command, check=True)
            logger.info(f"Added metadata to track:{track.title}")
        except subprocess.CalledProcessError as e:
            logger.info(f"Error adding metadata to track {track.title}: {e}")