#INSTRUCTIONS on the options.
print("Hello, there here are your options.")
print('Rock')
print('Paper')
print('Scissors')


#Is preparing the input, and creating variables.
Player1 = input('Player1, make your move!')
Player2 = input('Player2, make your move!')

#Decides who won.
if Player1 == 'Rock' and Player2 == 'Paper':
    print('Player2 has won!(Sorry player 1)')

elif Player1 == 'Rock' and Player2 == 'Scissors':
    print("Player1 has won!")

elif Player1 == "Paper" and Player2 == "Scissors":
    print('Player2 has won!')

elif Player1 == "Paper" and Player2 == "Rock":
    print('Player1 has won!')

elif Player1 == 'Scissors' and Player2 == 'Rock':
    print('Player2 has won!')

elif Player1 == 'Scissors' and Player2 == "Paper":
    print('Player1 has won!')

elif Player1 == Player2:
    print("It's a tie.")
else:
    print('HEY YOU DID SOMETHING WRONG TRY AGAIN.')