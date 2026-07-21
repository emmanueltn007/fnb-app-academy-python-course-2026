# The Challenge: “The High-Score Tracker Game”

while True:
    game_score = input("Enter your game score: ")
    
    if game_score.strip().lower() == "stop":
        print("Game session ended!")
        break
    else:
        if int(game_score) > 100:
            print("Wow! That’s a new high score!")
        else:
            print("Good try, keep playing!")
