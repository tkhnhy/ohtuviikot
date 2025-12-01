class TennisGame:
    # Class Constants
    POINT_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    DEUCE_THRESHOLD = 3  # The score (3 points) at which Deuce logic begins
    
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def get_score(self):
        if self.p1_score == self.p2_score:
            return self._get_tied_score()
        elif self.p1_score > self.DEUCE_THRESHOLD or self.p2_score > self.DEUCE_THRESHOLD:
            return self._get_end_game_score()
        else:
            return self._get_regular_score()

    # Helper Methods

    def _get_tied_score(self):
        if self.p1_score < self.DEUCE_THRESHOLD:
            # Returns "Love-All", "Fifteen-All", or "Thirty-All"
            return f"{self.POINT_NAMES[self.p1_score]}-All"
        return "Deuce"

    def _get_end_game_score(self):
        score_difference = self.p1_score - self.p2_score

        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _get_regular_score(self):
        p1_term = self.POINT_NAMES[self.p1_score]
        p2_term = self.POINT_NAMES[self.p2_score]
        return f"{p1_term}-{p2_term}"