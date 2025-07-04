import os, subprocess

def audio_split(input_file: str, output_dir: str, concert):
    for i, track in enumerate(concert.tracks):
        start_time = track.start
        end_time = track.end
        output_file = os.path.join(output_dir, f"{i}. {track.title}.mp3")

        command = [
            "ffmpeg",
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
            print(f"\033[31mSplit and saved track: {track.title}. start: {start_time}, end: {end_time}\033[0m")
        except subprocess.CalledProcessError as e:
            print(f"Error splitting track {track.title}: {e}")