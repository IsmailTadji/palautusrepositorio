from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3



class StatisticsService:
    def __init__(self, reader):
        self._reader = reader
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=None):
        # metodin käyttämä apufufunktio voidaan määritellä näin
        sort_types = {
            SortBy.POINTS: lambda player: player.points,
            SortBy.GOALS: lambda player: player.goals,
            SortBy.ASSISTS: lambda player: player.assists,
        }
        if sort_by in sort_types:
            sort_type = sort_types[sort_by]
        else:
            sort_type = lambda player: player.points

        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_type
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
