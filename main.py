from core import processor
from config_loader import load_concert
import os, click

"""
TO DO

2. make prettier cli with rich
"""


def validate_concert(json_file):
    # Try to load the concert configuration from a JSON file
    try:
        print(f"Loading concert from {json_file}...")
        concert = load_concert(json_file)  # Load the concert configuration
        print("Concert configuration loaded successfully.")
        return concert
    except Exception as e:
        # If there's an error loading the concert config, print it and exit
        print(f"Error loading concert configuration: {e}")
        exit(1)

@click.command()
@click.argument("json_file", type=click.Path(exists=True, dir_okay=False, readable=True))
def main(json_file):
    print(json_file)
    os.makedirs("./temp", exist_ok=True)
    concert = validate_concert(json_file)
    processor.pipeline(concert)



if __name__ == "__main__":
    main()
    


