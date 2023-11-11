import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_players(self):

        players = []

        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
            
        return players

class PlayerStats:
    def __init__(self, response):
        self.response = response

    def top_scorers_by_nationality(self, nationality):
        players = self.response.get_players()
        print(f'players from {nationality}')
        players = sorted(players, key=lambda player: player.points, reverse=True)
        players_sorted = []
        for player in players:
            if player.nationality == nationality:
                players_sorted.append(player)
        return players_sorted


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
