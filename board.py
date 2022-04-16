board = [["-" for i in range(3)] for j in range(3)]
def print_board():
    print("Printing board")
    for row in board:
        print(row)
if _name_ == "_main_":
    print_board()