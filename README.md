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
You need the following things installed for this to work.
* [Python.](https://www.python.org/)
* [FFmpeg.](https://www.gyan.dev/ffmpeg/builds/)
### Setup
1. Clone this repository.
   ```
   git clone https://github.com/mrbanana55/Concert_Downloader.git
   ```
2. Create a virtual enviroment (optional).
3. Install dependencies.
   ```
   pip install -r requirements.txt
   ```
5. If you want to run it from anywhere, add the project folder to your system's path.
    1. Change `path/to/main.py` to your absolute path for the main.py file inside `concert_downloader.bat`.
    2. Add the absolute path of the folder to your system's environment variables.
    3. now you should be able to call it like `concert_downloader path\to\your_config.json`
##  Usage
You need to create a JSON file like the example ones and pass it as a concert_downloader parameter like this:
```
concert-downloader path/to/config.json
```
```
python main.py path/to/config.json
```
### Example 1: Local Video or Audio File
```
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
### Example 2: Youtube Video
```
{
  "source_type": "yotube",
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
#### Note
The following parameters are optional:
  * number.
  * artist.
  * album.
  * cover_image.
## Output
After running the conncert_downloader you will get individual .mp3 files per track with their respective metadata.
