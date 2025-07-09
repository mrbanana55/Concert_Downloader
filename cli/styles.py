from rich.console import Console
from rich.theme import Theme
custom_theme = Theme({
    "error_title": "blink bold white on red",
    "error_message": "underline red",

    "success_title": "blink bold white on green",
    "success_message": "underline green",
    
    "important": "magenta",
    "important_bold": "bold magenta",

    "info_title": "bold blue",
    "info_text": "blue",
})
console = Console(theme=custom_theme)