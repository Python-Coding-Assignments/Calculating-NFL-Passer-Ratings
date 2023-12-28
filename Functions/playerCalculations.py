def getPlayerStats(player):
    """This function calculates a football player's passer rating.  This function takes in a dictionary as an argument by main.py as its only parameter.  This function then returns the player's passer ratting, accurate to one decimal place, as a float."""

    #conditional statement which runs if the number of attempts is greater than zero
    if player["attempts"] > 0:
        #declarations and initialization of variables
        a = ((player["completions"] / player["attempts"]) - 0.3) * 5
        b = ((player["passingYards"] / player["attempts"]) - 3) * 0.25
        c = ((player["touchdowns"] / player["attempts"])) * 20
        d = 2.375 - ((player["interceptions"] / player["attempts"]) * 25)
        array = [a, b, c, d]
        passerRating = 0

        #for loop which iterates through each element of the array
        for i in range(0, len(array)):
            #conditional statement which changes value of a if a is greater than 2.375
            if array[i] > 2.375:
                array[i] = 2.375
            #conditional statement which changes value of a if a is less than 0     
            elif array[i] < 0:
                array[i] = 0   

        #initializing passerRating variable
        passerRating = float("{:.1f}".format(((array[0] + array[1] + array[2] + array[3]) / 6) * 100))

    #conditional statement which runs if the number of attempts is equal to zero
    else:
        passerRating = 0

    #returning passerRating variable
    return passerRating