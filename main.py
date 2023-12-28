from Functions import getPlayerRatings, getPlayerStats, getPlayerInfo

#declarations of two dictionaries
playerA = playerB = {}

#welcoming and initializing dictionaries for player A and player B
print("Welcome to the NFL Quarterback Passer Rating Calculator!\n")
print("Enter single game information for Player A:")
#initializing playerA dictionary
playerA = getPlayerInfo()
print("\nEnter single game information for Player B:")
#initializing playerB dictionary
playerB = getPlayerInfo()

#getting passer rating for player A and player B and adding element to dictionary
playerA["rating"] = getPlayerStats(playerA)
playerB["rating"] = getPlayerStats(playerB)

#comparing playerA's and playerB's passer ratings
getPlayerRatings(float(playerA["rating"]), float(playerB["rating"]))