import random

board = ["☐", "☐", "☐",
         "☐", "☐", "☐",
         "☐", "☐", "☐"]


# board = range(0, 9)


def show_board():
    print(board[0], "|", board[1], "|", board[2], "|")
    print("- - " * 3)
    print(board[3], "|", board[4], "|", board[5], "|")
    print("- - " * 3)
    print(board[6], "|", board[7], "|", board[8], "|")
    # print("☐", "|", "☐", "|", "☐", "|")
    # print("- - " * 3)
    # print("☐", "|", "☐", "|", "☐", "|")
    # print("- - " * 3)
    # print("☐", "|", "☐", "|", "☐", "|")


show_board()


def checkLine(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True
    else:
        return False


def checkAll(char):
    if checkLine(char, 0, 1, 2):
        return True
    if checkLine(char, 3, 4, 5):
        return True
    if checkLine(char, 6, 7, 8):
        return True
    if checkLine(char, 0, 3, 6):
        return True
    if checkLine(char, 1, 4, 7):
        return True
    if checkLine(char, 2, 5, 8):
        return True
    if checkLine(char, 0, 4, 8):
        return True
    if checkLine(char, 2, 4, 6):
        return True


# def checkForTie(char,spot1,spot2,spot3):
#     if board[spot1]!=char and board[spot2]!=char and board[spot3]!=char:
#         return True

playing_Status = True
while playing_Status:
    userInput = int(input("Select a spot: "))
    # if board[userInput != "x" and board[userInput] != "o":
    #     board[userInput]="X"
    if board[userInput] != "✘" and board[userInput] != "⭕" and board[userInput] == "☐":
        board[userInput] = "✘"
        if checkAll("✘"):
            print("Player X WINS!!!")

            playing_Status = False
            break

        # checking for a winner
        while True:

            # We now generate a random value between (0-8) to place a tic on our board
            random.seed()
            pc_Opponent = random.randint(0, 8)

            if board[pc_Opponent] != "✘" and board[pc_Opponent] != "⭕":
                board[pc_Opponent] = "⭕"

                if checkAll("⭕"):
                    print("Player ⭕ WINS!!!")
                    playing_Status = False
                    break
                break

    else:
        print("This spot is taken!")
    show_board()
