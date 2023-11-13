import unittest
from statistics_service import StatisticsService
from player import Player
from statistics_service import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        self.assertEqual("Semenko", self.stats.search("Semenko").name)
        self.assertEqual("EDM", self.stats.search("Semenko").team)
        self.assertEqual(4, self.stats.search("Semenko").goals)
        self.assertEqual(12, self.stats.search("Semenko").assists)
        self.assertIsNone(self.stats.search("Smenko"))


    def test_team(self):
        edm = self.stats.team("EDM")
        self.assertEqual(len(edm), 3)
        for player in edm:
            self.assertEqual(player.team, "EDM")

    def test_top(self):
        players = self.stats.top(4)
        self.assertEqual(len(players), 5)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")
        self.assertEqual(players[3].name, "Kurri")
        self.assertEqual(players[4].name, "Semenko")

    def test_top_filtered(self):
        top_goals = self.stats.top(2, SortBy.GOALS)
        self.assertEqual(top_goals[0].name, "Lemieux")
        self.assertEqual(top_goals[1].name, "Yzerman")
        
        top_assists = self.stats.top(2, SortBy.ASSISTS)
        self.assertEqual('Gretzky', top_assists[0].name)
        self.assertEqual("Yzerman", top_assists[1].name)

        top_points = self.stats.top(2, SortBy.POINTS)
        self.assertEqual('Gretzky', top_points[0].name)
        self.assertEqual("Lemieux", top_points[1].name)

if __name__ == "__main__":
    unittest.main()