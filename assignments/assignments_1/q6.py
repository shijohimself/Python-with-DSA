games_played = int(input("Total played: "))
games_won = int(input("Total won: "))
games_lost = int(input("Total lost: "))

games_tied = games_played - (games_won + games_lost)
total_points = (games_won * 4) + (games_tied * 2)
print(games_tied,total_points)