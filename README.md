# 🎶 Concert_Downloader



**Concert_Downloader** is a CLI tool that turns a YouTube or local video/audio concert into individually tagged MP3 tracks — complete with metadata and optional cover images.

---

## ✨ Features

- ✅ Supports both YouTube videos and local media files.
- 🎧 Splits full concerts into individual tracks based on a JSON config.
- 🏷️ Adds metadata: title, artist, album, track number, and album art.
- 📁 Outputs clean, organized MP3 files ready for your music library.

---
## 🛠️ Installation

### Prerequisites
You'll need the following installed on your system:
* [Python.](https://www.python.org/)
* [FFmpeg.](https://www.gyan.dev/ffmpeg/builds/)
### Setup
1. Clone this repository.
   ```bash
   git clone https://github.com/mrbanana55/Concert_Downloader.git
   cd Concert_Downloader
   ```
2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. (Optional) If you want to run it from anywhere:
   * Edit the `concert_downloader.bat` file and replace `path/to/main.py` with the absolute path to your `main.py` file.
   * Add the folder containing `concert_downloader.bat` to your system’s PATH.
   * Now you can call it like this:
     ```bash
     concert_downloader path/to/config.json 
     ```
##  🚀 Usage
You need to pass a JSON config file as an argument. You can run it like:
```bash
python main.py path/to/config.json
# or, if using .bat setup:
concert_downloader path/to/config.json
```
## Example Configs
### Local File Example
```json
{
  "source_type": "local",
  "file_source": "C:/path/to/concert_audio.mp4",
  "artist": "Artist Example",
  "album": "Album Example",
  "cover_image": "C:/your/image.jpg",
  "output_dir": "C:/your/output/folder",
  "duration": "00:30:54",
  "tracks": [
    {
      "title": "Song 1",
      "start": "00:00:00",
      "number": 1
    },
    {
      "title": "Song 2",
      "start": "00:04:17",
      "number": 2
    },
    {
      "title": "Song 3",
      "start": "00:08:30",
      "number": 3
    }
  ]
}

```
### YouTube Example
```json
{
  "source_type": "youtube",
  "video_url": "https://www.youtube.com/watch?v=example_video_id",
  "artist": "Artist Example",
  "album": "Album Example",
  "cover_image": "C:/your/image.jpg",
  "output_dir": "C:/your/output/folder",
  "duration": "00:30:54",
  "tracks": [
    {
      "title": "Song 1",
      "start": "00:00:00",
      "number": 1
    },
    {
      "title": "Song 2",
      "start": "00:04:17",
      "number": 2
    },
    {
      "title": "Song 3",
      "start": "00:08:30",
      "number": 3
    }
  ]
}
```
## Optional Fields
| Field        | Description                       |
|--------------|-----------------------------------|
| `artist`     | Used for metadata (defaults to blank) |
| `album`      | Used for metadata (defaults to blank) |
| `cover_image`| Embed album art if provided       |
| `number`     | Track number for ordering         |

## Output
After running `concert_downloader` you will get individual `.mp3` files per track with their respective metadata.
