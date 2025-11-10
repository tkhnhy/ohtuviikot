import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    fin_players = []

    for player in players:
        if player.nationality == "FIN":
            fin_players.append(player)
    
    fin_players.sort(key=lambda x: x.score, reverse=True)
    print("Players from FIN:")
    for player in fin_players:
        print(f"{player}, Team: {player.team}, {player.goals} + {player.assists} = {player.score}")

if __name__ == "__main__":
    main()

