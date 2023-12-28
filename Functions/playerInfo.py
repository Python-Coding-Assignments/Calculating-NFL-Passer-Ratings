def getPlayerInfo():
    """getPlayerInfo is a function that gets information from the user about a player's statistics.  The function also ensures that only valid integers are entered in by the user.  For example, this function checks to make sure that the user input is not a number less than or equal to zero.  Afterwards, the function returns a list containing the player's information."""

    #declaration and initialization of variables
    attempts = completions = passingYards = touchdowns = interceptions = -1
    counter = 0
    profile = [attempts, completions, passingYards, touchdowns, interceptions]
    profileValue = ["Attempts: ", "Completions: ", "Passing Yards: ", "Touchdowns: ", "Interceptions: "]
    dictionary = {"attempts": 0, "completions": 0, "passingYards": 0, "touchdowns": 0, "interceptions": 0}

    #for loop which iterates through each element of the list
    for i in range(0, len(profile)):
        #while loop checking each element of list to ensure every element is a positive integer
        while profile[i] < 0:
            #getting list value user's input
            profile[i] = int(input(profileValue[i]))   

    #for loop which iterates through each key of dictionary
    for key in dictionary.keys():
        #initializing the keys in dictionary
        dictionary[key] = profile[counter]
        #incrementing counter by one
        counter += 1                 

    #returning dictionary
    return dictionary