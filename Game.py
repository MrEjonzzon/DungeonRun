def playerselection(choice):
    if choice == 1:
        Player = Knight
    elif choice == 2:
        Player = Mage
    elif choice == 3:
        pPlayer = Thief
    else:
        print("Invalid Choice")

bajs = int(input("what do u wanan be "))

playerselection(bajs)




