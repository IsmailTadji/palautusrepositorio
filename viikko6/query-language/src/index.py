from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, All, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
        )


    for player in stats.matches(matcher):
        print(player)
    
    
    filtered_with_all = stats.matches(All())
    
    print(len(filtered_with_all))



if __name__ == "__main__":
    main()
