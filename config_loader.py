from pydantic import BaseModel, HttpUrl, FilePath, field_validator
from typing import List, Optional, Literal
import json, datetime


class Track(BaseModel):
    title: str
    start: str
    end: str
    number: Optional[int] = None

class Config(BaseModel):
    source_type: Literal['youtube', 'local']
    video_url: Optional[HttpUrl] = None
    source: Optional[str] = None
    artist: Optional[str] = None
    album: Optional[str] = None
    cover_image: Optional[FilePath] = None
    output_format: Literal['mp3', 'flac'] = 'mp3'
    tracks: List[Track]



def load_concert(path: str) -> Config:
    with open(path) as f:
        data = json.load(f)
    return Config(**data)