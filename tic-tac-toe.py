
pieces = {}
columns = ['A', 'B', 'C']
rows = [1, 2, 3]

for x in columns:
    letter = x
    pieces[letter] = {}
    for y in rows:
            pieces[letter][y] = " "
            
        
game = {
    'player1Turn': True,
    'playerScore': 0,
    'player2Score': 0,
    'currentPiece': 'X',
    'board': '',
    'turn': 0
}



def render():
    game["board"] = f'     A   B   C    \n1)   {pieces["A"][1]} | {pieces["B"][1]} | {pieces["C"][1]} \n    ------------\n2)   {pieces["A"][2]} | {pieces["B"][2]} | {pieces["C"][2]} \n    ------------\n3)   {pieces["A"][3]} | {pieces["B"][3]} | {pieces["C"][3]} '
    print(game["board"])

def start():
    response = input("A ----------------------\nLet's play Py-Pac-Poe!\n----------------------\nReady To Play? (y/N):")
    responseCaps = response.upper()
    if responseCaps == "Y":
        render()
        print('Game Started!!')
        determineTurn()
    else:
        print('Ok Bye')


def determineTurn():
    if game["player1Turn"]:
        player = 'Player 1'
        game["currentPiece"] = 'X'
    else:
        player = 'Player 2'
        game["currentPiece"] = 'O'

    turn(player)

def turn(player):
    response = input(f"Player {player}'s Move (example B2):")
    if len(response) == 2:
        column = response[0]
        row = int(response[1])
    else:
        print(f"Invalid Entry! Player {player}'s Move (example B2):")
        return turn(player)

    placeXOrO(column, row, player)

def placeXOrO(col, row, player):
    if pieces[col][row] == " ":
        pieces[col][row] = game["currentPiece"]
        render()
        game["turn"] += 1
        game["player1Turn"] = not game["player1Turn"]
        determineWinner(player)
    else:
        print('INVALID MOVE YOU CHEATER!!')
        return turn(player)

def checkVictoryRows():
    for row in rows:
        winner = True
        for col in columns:
            if pieces[col][row] != game["currentPiece"]:
                winner = False
        if winner == True:
            return True

def checkVictoryCols():
    for col in columns:
        winner = True
        for row in rows:
            if pieces[col][row] != game["currentPiece"]:
                winner = False
        if winner == True:
            return True

def checkVictoryDiags():
    if pieces["A"][1] == game["currentPiece"] and pieces["B"][2] == game["currentPiece"] and pieces["C"][3] == game["currentPiece"]:
        print('Winner')
        return True
    elif pieces["A"][3] == game["currentPiece"] and pieces["B"][2] == game["currentPiece"] and pieces["C"][1] == game["currentPiece"]:
        return True

def determineWinner(player):
    if checkVictoryDiags() or checkVictoryRows() or checkVictoryCols():
        if player == "Player 1":
            print("Player 1 Wins!!!")
        elif player == "Player 2":
            print("Player 2 Wins!!!")
    elif game["turn"] == 9:
            print("Its a tie!!!")
    else:
        determineTurn()

# and call the start function
start()

