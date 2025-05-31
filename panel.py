from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.style import Style
import json

def Panel():
    with open("./utils/config.json", "r") as json_file:
        data = json.load(json_file)
    print(" ")

    ascii_title = Text("""
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣾⡿⠟⠋⠁⠀⠀⠀⠀⠈⠙⠻⣿⣷⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⣿⠟⠁⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠈⠻⣿⣆⠀⠀⠀⠀
⠀⠀⠀⣼⣿⠁⠀⣠⣶⣿⣿⠿⠿⠿⠿⣿⣿⣿⣷⣦⡀⠀⠘⣿⣧⠀⠀⠀
⠀⠀⣼⣿⠃⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⢀⣽⣿⣿⠃⠀⠐⣿⣿⠀⠀⠀
⠀⠀⣿⣿⠀⠀⠀⠙⢿⣿⣦⣀⠀⠀⣀⣤⣿⣿⠟⠁⠀⠀⠀⣿⣿⠀⠀⠀
⠀⠀⢿⣿⣦⣀⠀⠀⠀⠉⠛⠿⣿⣿⠿⠛⠉⠀⠀⠀⢀⣀⣴⣿⡿⠀⠀⠀
⠀⠀⠀⠛⠿⣿⣿⣶⣦⣤⣤⣄⣀⣀⣤⣤⣴⣶⣿⣿⠿⠿⠛⠋⠀⠀⠀⠀

██████╗ ██╗███████╗ ██████╗  ██████╗  ██████╗ ██████╗  ██████╗ ██╗███████╗
██╔══██╗██║██╔════╝██╔════╝ ██╔═══██╗██╔════╝ ██╔══██╗██╔═══██╗██║██╔════╝
██║  ██║██║█████╗  ██║  ███╗██║   ██║██║  ███╗██████╔╝██║   ██║██║█████╗  
██║  ██║██║██╔══╝  ██║   ██║██║   ██║██║   ██║██╔═══╝ ██║   ██║██║██╔══╝  
██████╔╝██║███████╗╚██████╔╝╚██████╔╝╚██████╔╝██║     ╚██████╔╝██║███████╗
╚═════╝ ╚═╝╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝      ╚═════╝ ╚═╝╚══════╝

        SISTEMA DE CÓPIA DE SERVIDORES | PORTUGUÊS | TERMUX
""", style="bold red")

    console = Console()
    console.print(ascii_title)

    # Estilo dos status
    on_style = Style(color="green", bold=True)
    off_style = Style(color="red", bold=True)

    # Tabela de configurações
    table = Table(title="DISCORD COPI | Configurações", show_header=True, header_style="bold magenta")
    table.add_column("Função", style="cyan", width=30)
    table.add_column("Status", justify="center", width=10)

    for setting, status in data["copy_settings"].items():
        status_text = Text("ON" if status else "OFF", style=on_style if status else off_style)
        table.add_row(setting.replace("_", " ").capitalize(), status_text)

    console.print(table)


def Panel_Run(guild, user):
    with open("./utils/config.json", "r") as json_file:
        data = json.load(json_file)
    print(" ")

    ascii_title = Text("""
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣴⣶⣶⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣾⡿⠟⠋⠁⠀⠀⠀⠀⠈⠙⠻⣿⣷⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣰⣿⠟⠁⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠈⠻⣿⣆⠀⠀⠀⠀
⠀⠀⠀⣼⣿⠁⠀⣠⣶⣿⣿⠿⠿⠿⠿⣿⣿⣿⣷⣦⡀⠀⠘⣿⣧⠀⠀⠀
⠀⠀⣼⣿⠃⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⢀⣽⣿⣿⠃⠀⠐⣿⣿⠀⠀⠀
⠀⠀⣿⣿⠀⠀⠀⠙⢿⣿⣦⣀⠀⠀⣀⣤⣿⣿⠟⠁⠀⠀⠀⣿⣿⠀⠀⠀
⠀⠀⢿⣿⣦⣀⠀⠀⠀⠉⠛⠿⣿⣿⠿⠛⠉⠀⠀⠀⢀⣀⣴⣿⡿⠀⠀⠀
⠀⠀⠀⠛⠿⣿⣿⣶⣦⣤⣤⣄⣀⣀⣤⣤⣴⣶⣿⣿⠿⠿⠛⠋⠀⠀⠀⠀

██████╗ ██╗███████╗ ██████╗  ██████╗  ██████╗ ██████╗  ██████╗ ██╗███████╗
██╔══██╗██║██╔════╝██╔════╝ ██╔═══██╗██╔════╝ ██╔══██╗██╔═══██╗██║██╔════╝
██║  ██║██║█████╗  ██║  ███╗██║   ██║██║  ███╗██████╔╝██║   ██║██║█████╗  
██║  ██║██║██╔══╝  ██║   ██║██║   ██║██║   ██║██╔═══╝ ██║   ██║██║██╔══╝  
██████╔╝██║███████╗╚██████╔╝╚██████╔╝╚██████╔╝██║     ╚██████╔╝██║███████╗
╚═════╝ ╚═╝╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝      ╚═════╝ ╚═╝╚══════╝

        SISTEMA DE CÓPIA DE SERVIDORES | PORTUGUÊS | TERMUX
""", style="bold red")

    console = Console()
    console.print(ascii_title)

    on_style = Style(color="green", bold=True)
    off_style = Style(color="red", bold=True)

    table = Table(title=f"Servidor: {guild} | Usuário: {user}", show_header=True, header_style="bold magenta")
    table.add_column("Função", style="cyan", width=30)
    table.add_column("Status", justify="center", width=10)

    for setting, status in data["copy_settings"].items():
        status_text = Text("ON" if status else "OFF", style=on_style if status else off_style)
        table.add_row(setting.replace("_", " ").capitalize(), status_text)

    console.print(table)
