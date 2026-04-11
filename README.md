# Concert_Downloader

**Concert_Downloader** is a CLI tool that turns a YouTube or local video/audio concert into individually tagged MP3 tracks — complete with metadata and optional cover images.

---

## Features

- Supports both YouTube videos and local media files.
- Splits full concerts into individual tracks based on a JSON config.
- Adds metadata: title, artist, album, track number, and album art.
- Outputs clean, organized MP3 files ready for your music library.

---

## Installation

### Prerequisites

You'll need the following installed on your system:

- [Python 3.9+](https://www.python.org/)
- [FFmpeg](https://www.ffmpeg.org/download.html) (Ensure it is in your system's PATH)

### Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/mrbanana55/Concert_Downloader.git
   cd Concert_Downloader
   ```

2. Install the package:
   ```bash
   pip install .
   ```
   or if you want to use it globally:
   ```bash
   pipx install .
   ```

---

## Usage

Once installed, you can use the `concert_downloader` command from anywhere:

```bash
concert_downloader path/to/config.json
```

### Example Configs

#### Local File Example

```json
{
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
}
```

#### YouTube Example

```json
{
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
}
```

## Configuration Fields

| Field         | Required | Description                                               |
| ------------- | -------- | --------------------------------------------------------- |
| `source_type` | Yes      | `youtube` or `local`                                      |
| `video_url`   | Yes\*    | YouTube URL (required if `source_type` is `youtube`)      |
| `file_source` | Yes\*    | Path to local file (required if `source_type` is `local`) |
| `artist`      | No       | Used for metadata                                         |
| `album`       | No       | Used for metadata                                         |
| `duration`    | Yes      | Total duration of the concert (`HH:MM:SS`)                |
| `cover_image` | No       | Path to an image file to embed as album art               |
| `output_dir`  | Yes      | Directory where tracks will be saved                      |
| `tracks`      | Yes      | List of tracks with `title`, `start`, and `number`        |

---

## Output

After running `concert_downloader`, you will get individual `.mp3` files in your specified `output_dir`, each tagged with the provided metadata and album art.
