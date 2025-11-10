from rich.console import Console
from rich.table import Table
from player import Player
from playerReader import PlayerReader
from playerStats import PlayerStats

def main():
    seasons = ["2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26"]
    nationalities = ["USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS"]
    
    console = Console()
    console.print("[bold green]Seasons:[/bold green] " + ", ".join(seasons))
    season = str(input("Enter season: "))
    console.print("[bold green]Nationalities:[/bold green] " + ", ".join(nationalities))
    nationality = str(input("Enter nationality: "))
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality(nationality)



    table = Table(title=f"Season {season} players from {nationality}")

    table.add_column("Name", style="bold cyan")
    table.add_column("Team", style="bold red")
    table.add_column("Goals", justify="right", style="green")
    table.add_column("Assists", justify="right", style="green")
    table.add_column("Score", justify="right", style="green")

    for player in players:
        table.add_row(
            str(player),
            str(player.team),
            str(player.goals),
            str(player.assists),
            str(player.score)
        )

    console.print(table)

if __name__ == "__main__":
    main()

