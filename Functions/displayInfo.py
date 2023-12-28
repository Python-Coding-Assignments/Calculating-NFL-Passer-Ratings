def getPlayerRatings(playerA, playerB):
    """getPlayerRatings is a function that prints data to the console about information comparing two players' passer ratings.  This function takes in two arguments: playerA and playerB.  These two arguments are of type float represent the players' passer ratings.  The function then returns a series of statement if certain conditions are met."""

    #printing both players' passer ratings to the console
    print("\nPlayer A's single game passer rating:" + str(playerA))
    print("Player B's single game passer rating:" + str(playerB))

    #conditional statement which runs if playerA's passer rating is greater than playerB's passer rating
    if playerA > playerB:
        print("Player A was better than Player B by a difference of " + "{:.1f}".format(playerA - playerB))
    #conditional statement which runs if playerB's passer rating is greater than playerA's passer rating    
    elif playerB > playerA:
        print("Player B was better than Player A by a difference of " + "{:.1f}".format(playerB - playerA))
    #conditional statement which runs if both players' passer ratings are the same    
    else:
        print("Player A and B have the same rating!")

    #conditional statement which runs if playerA's passer rating is perfect
    if playerA >= 158.3:
        print("\nPlayer A had a PERFECT passer rating.")

    #conditional statement which runs if playerB's passer rating is perfect    
    if playerB >= 158.3:
        print("\nPlayer B had a PERFECT passer rating.")            