from pydantic import BaseModel, HttpUrl, FilePath, DirectoryPath
from typing import List, Optional, Literal
import json


class Track(BaseModel):
    title: str
    start: str
    end: str
    number: Optional[int] = None

class Concert(BaseModel):
    source_type: Literal['youtube', 'local']
    video_url: Optional[HttpUrl] = None
    file_source: Optional[FilePath] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    cover_image: Optional[FilePath] = None
    output_format: Literal['mp3', 'flac'] = 'mp3'
    tracks: List[Track]
    output_dir: DirectoryPath

def load_concert(path: str) -> Concert:
    with open(path) as f:
        data = json.load(f)
    return Concert(**data)