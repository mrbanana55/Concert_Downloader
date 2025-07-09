from cli.styles import console
from rich.table import Table
from config_loader import load_concert

def render_json(json):
    table = Table(title="\nConcert Songs", show_lines=True)
    table.add_column('[info_title]Song Title[/info_title]', justify='left')
    table.add_column('[info_title]Song Number[/info_title]', justify='center')
    table.add_column('[info_title]Song Start Time[/info_title]', justify='right')

    for track in json.tracks:
        table.add_row(
            track.title,
            str(track.number),
            track.start
        )
    console.print(table)