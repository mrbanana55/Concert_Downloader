import subprocess, ffmpeg

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