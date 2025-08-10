from rich.prompt import Prompt


# Just the style tags
SUCCESS = "[bold green]"
ERROR = "[bold red]"
WARNING = "[bold yellow]"
INFO = "[bold blue]"
RESET = "[/]"

# New prompt style
def ask(text, style="bold cyan"):
    """One-line styled prompts where EVERYTHING is cyan."""
    return Prompt.ask(f"[{style}]>>> {text}[/]")

