from core import processor
from config_loader import load_concert
from cli.styles import console
from cli.render_json import render_json
import os, click
from plyer import notification



def validate_concert(json_file):
    # Try to load the concert configuration from a JSON file
    try:
        concert = load_concert(json_file)  # Load the concert configuration
        return concert
    except Exception as e:
        # If there's an error loading the concert config, print it and exit
        console.print(f"[error_title]Error loading concert configuration:[/error_title] [error_message]{e}[/error_message]")
        exit(1)

@click.command()
@click.argument("json_file", type=click.Path(exists=True, dir_okay=False, readable=True))
def main(json_file):
    
    os.makedirs("./temp", exist_ok=True)

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
    os.rmdir("./temp")
    notification.notify(
        title="Concert Processing Complete",
        message=f"Songs are located at: {concert.output_dir}",
        app_name="Concert Processor",
        timeout=5
    )


if __name__ == "__main__":
    main()
    


