class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
            score = ""

            if self.m_score1 == self.m_score2:
                score = self.get_equal_score()
            elif self.m_score1 >= 4 or self.m_score2 >= 4:
                score = self.get_advantage_or_winner()
            else:
                score = self.get_regular_score()

            return score

    def get_equal_score(self):
        if self.m_score1 == 0:
            return "Love-All"
        elif self.m_score1 == 1:
            return "Fifteen-All"
        elif self.m_score1 == 2:
            return "Thirty-All"
        else:
            return "Deuce"

    def get_advantage_or_winner(self):
        minus_result = self.m_score1 - self.m_score2

        if minus_result == 1:
            return f"Advantage {self.player1_name}"
        elif minus_result == -1:
            return f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def get_regular_score(self):
        score = ""
        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                score += "-"
                temp_score = self.m_score2

            score += self.get_score_description(temp_score)

        return score

    def get_score_description(self, temp_score):
        if temp_score == 0:
            return "Love"
        elif temp_score == 1:
            return "Fifteen"
        elif temp_score == 2:
            return "Thirty"
        elif temp_score == 3:
            return "Forty"
