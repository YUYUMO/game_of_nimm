def main():
    """
    A program to play Nimm. 
    Nimm is an ancient game of strategy that is named after the old German word for "take." It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate taking stones until there are zero left. The game of Nimm goes as follows:
    The game starts with a pile of 20 stones between the players
    The two players alternate turns
    On a given turn, a player may take either 1 or 2 stone from the center pile
    The two players continue until the center pile has run out of stones.
    The last player to take a stone loses.
    """
    #create a variable to store the number of stones
    stones_num = 20
    # create a variable to indicate the player. 1 means player 1, 2 means player 2
    current_player = 1 
    # create a function to switch player
    def switch_player(current_player):
        if current_player == 1:
            return 2
        else:
            return 1
    #repeat the following as long as the number of stones > 0
    while(stones_num > 0):
    #print a statement to indicate the current number of stones
        print(f"There are {stones_num} stones left.")
    #get the user's input on 1 or 2 stones he/she would like to remove
        user_action = input(f"Player {current_player} would you like to remove 1 or 2 stones? ")
        #keeps explaining to the user that he/she needs to enter a 1 or 2 integer if his/her input is invalid
        while user_action != "1" and user_action != "2":
            user_action = input("Please enter 1 or 2: ")
        #perform the following if the user's input is not an empty string and is a digit
        if user_action != "" and user_action.isdigit():
            #convert the user's input into an integer and minus the stones number by the user's number
            user_number = int(user_action)
            stones_num = stones_num - user_number
            #switch player for the next round
            current_player = switch_player(current_player)
    #print an empty line
        print("")
    #print the winner when there are no stones left
    print(f"Player {current_player} wins!")


if __name__ == '__main__':
    main()