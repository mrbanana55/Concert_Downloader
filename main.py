from core import processor
from config_loader import load_concert
import os

json_example = "example.json"

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

if __name__ == "__main__":

    os.makedirs("./temp", exist_ok=True)
    concert = validate_concert(json_example)
    processor.pipeline(concert)

