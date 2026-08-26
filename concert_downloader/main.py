from concert_downloader.core import processor
from concert_downloader.config_loader import load_concert
from concert_downloader.ui.styles import console
from concert_downloader.ui.render_json import render_json
from concert_downloader.errors import ConcertError
import click


def validate_concert(json_file):
    # Try to load the concert configuration from a JSON file
    try:
        concert = load_concert(json_file)  # Load the concert configuration
        return concert
    except Exception as e:
        # If there's an error loading the concert config, print it and exit
        raise ConcertError(f"Error loading concert configuration: {e}") from e


LOCAL_EXAMPLE = """{
  "source_type": "local",
  "file_source": "/path/to/concert_audio.mp4",
  "artist": "Artist Example",
  "album": "Album Example",
  "cover_image": "/your/image.jpg",
  "output_dir": "/your/output/folder",
  "duration": "00:30:54",
  "tracks": [
    { "title": "Song 1", "start": "00:00:00", "number": 1 },
    { "title": "Song 2", "start": "00:04:17", "number": 2 },
    { "title": "Song 3", "start": "00:08:30", "number": 3 }
  ]
}"""

YOUTUBE_EXAMPLE = """{
  "source_type": "youtube",
  "video_url": "https://www.youtube.com/watch?v=example_video_id",
  "artist": "Artist Example",
  "album": "Album Example",
  "cover_image": "/your/image.jpg",
  "output_dir": "/your/output/folder",
  "duration": "00:30:54",
  "tracks": [
    { "title": "Song 1", "start": "00:00:00", "number": 1 },
    { "title": "Song 2", "start": "00:04:17", "number": 2 },
    { "title": "Song 3", "start": "00:08:30", "number": 3 }
  ]
}"""

def print_examples():
    console.print("\n[important_bold]Local File Example:[/important_bold]")
    console.print(LOCAL_EXAMPLE)
    console.print("\n[important_bold]YouTube Example:[/important_bold]")
    console.print(YOUTUBE_EXAMPLE)

def print_missing_input_help():
    console.print("An input .json file is required to run the concert downloader.", style="error_message")
    console.print("Please provide a path to your .json file or use --example to see sample configurations.", style="info_text")
    console.print("For more help, visit: https://github.com/mrbanana55", style="important")

def print_help():
    console.print("[info_title]Concert Downloader CLI[/info_title]\n")
    console.print("Download and split concerts from YouTube or local files into individual tagged MP3 tracks.\n")
    console.print("[important_bold]Usage:[/important_bold]")
    console.print("  concert_downloader <JSON_FILE> [OPTIONS]\n")
    console.print("[important_bold]Arguments:[/important_bold]")
    console.print("  JSON_FILE       Path to the JSON configuration file containing concert info.\n")
    console.print("[important_bold]Options:[/important_bold]")
    console.print("  --example       Show sample JSON configuration files for local files and YouTube.")
    console.print("  -h, --help      Show this help message and exit.\n")
    console.print("[important_bold]Documentation & Issues:[/important_bold]")
    console.print("  https://github.com/mrbanana55")

@click.command(add_help_option=False)
@click.argument("json_file", required=False, type=click.Path(exists=True, dir_okay=False, readable=True))
@click.option("--example", is_flag=True, help="Show JSON configuration examples.")
@click.option("-h", "--help", is_flag=True, help="Show help message.")
def main(json_file, example, help):
    if example:
        print_examples()
        return

    if help:
        print_help()
        return

    if not json_file:
        print_missing_input_help()
        return

    with console.status("validating concert...", spinner="dots"):
        concert = validate_concert(json_file)
    console.print("Concert configuration loaded successfully.", style="success_message")
    
    render_json(concert)
    accept = console.input("\n[important]Press y to start processing the concert, or any other key to exit: [/important]")
    if accept.lower() != 'y':
        console.print("Exiting without processing the concert.", style="important")
        return
    console.print("Starting concert processing...", style="info_text")
    processor.pipeline(concert)
    console.print(f"Concert processing completed successfully. Songs are located at: {concert.output_dir}", style="success_title")


if __name__ == "__main__":
    main()
    


