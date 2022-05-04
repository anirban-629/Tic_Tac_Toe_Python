# 012
# 345
# 678

def printBoard(list1):
    print(f" {list1[0]}|{list1[1]}|{list1[2]}")
    print("--|-|--")
    print(f" {list1[3]}|{list1[4]}|{list1[5]}")
    print("--|-|--")
    print(f" {list1[6]}|{list1[7]}|{list1[8]}")

def checkX(list1):
    if list1[0] == 'X' and list1[1] == 'X' and list1[2] == 'X':
        return 1
    if list1[3] == 'X' and list1[4] == 'X' and list1[5] == 'X':
        return 1
    if list1[6] == 'X' and list1[7] == 'X' and list1[8] == 'X':
        return 1
    if list1[0] == 'X' and list1[3] == 'X' and list1[6] == 'X':
        return 1
    if list1[1] == 'X' and list1[4] == 'X' and list1[7] == 'X':
        return 1
    if list1[2] == 'X' and list1[5] == 'X' and list1[8] == 'X':
        return 1
    if list1[0] == 'X' and list1[4] == 'X' and list1[8] == 'X':
        return 1
    if list1[2] == 'X' and list1[4] == 'X' and list1[6] == 'X':
        return 1

def checkO(list1):
    if list1[0] == 'O' and list1[1] == 'O' and list1[2] == 'O':
        return 1
    if list1[3] == 'O' and list1[4] == 'O' and list1[5] == 'O':
        return 1
    if list1[6] == 'O' and list1[7] == 'O' and list1[8] == 'O':
        return 1
    if list1[0] == 'O' and list1[3] == 'O' and list1[6] == 'O':
        return 1
    if list1[1] == 'O' and list1[4] == 'O' and list1[7] == 'O':
        return 1
    if list1[2] == 'O' and list1[5] == 'O' and list1[8] == 'O':
        return 1
    if list1[0] == 'O' and list1[4] == 'O' and list1[8] == 'O':
        return 1
    if list1[2] == 'O' and list1[4] == 'O' and list1[6] == 'O':
        return 1

# def winner(list1):
#     a_list = list1.copy()
#     indices = []
#     for i in range(len(a_list)):
#         if a_list[i] == 'O':
#             indices.append(i)
#
#     def check(num, indices):
#         if num in indices:
#             return '#'
#         else:
#             return num
#
#     print(f"{check(0, indices)}|{check(1, indices)}|{check(2, indices)}")
#     print("-----")
#     print(f"{check(3, indices)}|{check(4, indices)}|{check(5, indices)}")
#     print("-----")
#     print(f"{check(6, indices)}|{check(7, indices)}|{check(8, indices)}")



if __name__ == '__main__':
    print("Welcome to Tic Tac Toe \n")
    list1=[
        0,1,2,
        3,4,5,
        6,7,8
    ]
    printBoard(list1)
    p1 = 10
    p2 = 11
    while(True):
        turn=0
        # Player 1
        p1=int(input("\nX position -> \n"))
        if p1==p2:
            print("Occupied By O Try Again:")
            p1=int(input("X position -> \n"))
        print("\n")
        list1[p1]='X'
        printBoard(list1)
        condX = checkX(list1)
        if (condX == 1):
            print("\nX own\n")
            # winner(list1)
            break

        # Player 2
        p2=int(input("\nO position -> \n"))
        if p2==p1:
            print("Occupied By X Try Again:")
            p2=int(input("O position -> \n"))
        list1[p2]='O'
        printBoard(list1)
        condO=checkO(list1)
        if(condO==1):
            print("\nO own\n")
            # winner(list1)
            break

        #Draw
        if(turn==8):
            print("Game Draw")
            break

