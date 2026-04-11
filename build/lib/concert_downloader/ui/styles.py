from rich.console import Console
from rich.theme import Theme
custom_theme = Theme({
    "error_title": "blink bold white on red",
    "error_message": "underline red",

    "success_title": "bold white green",
    "success_message": "underline green",
    
    "important": "magenta",
    "important_bold": "bold magenta",

    "info_title": "bold blue",
    "info_text": "blue",

    "progress_title": "bold yellow",
    "progress_message": "yellow",
})
console = Console(theme=custom_theme)