class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        
    def top_scorers_by_nationality(self, nationality):
        players_of_nationality = [
        player for player in self.reader.get_players()
        if player.nationality == nationality
        ]
        
        players_of_nationality = sorted(players_of_nationality, key=lambda x: x.score, reverse=True)
        
        
        return players_of_nationality