from core import processor
import os

if __name__ == "__main__":
    os.makedirs("./temp", exist_ok=True) #this may be in main.py
    processor.pipeline('example.json')