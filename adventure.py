# Project 2: Text Adventure
# Name: Kamar Billie-Fanning
# Date: October 2, 2026

health = 10
print(f"Health: {health}")

choice1 = input("Do you go left or right? ")

if choice1 == "left":
    health -= 2
    print(f"Health: {health}")
    
    choice2 = input("Do you fight or run? ")
    if choice2 == "fight":
        health += 4
        print(f"Health: {health}")
        
        choice3 = input("Do you take or leave? ")
        if choice3 == "take" and health > 0:
            print("=== YOU WIN ===")
        elif choice3 == "leave":
            print("=== GAME OVER ===")
        else:
            print("Invalid choice.")
    elif choice2 == "run":
        print("=== GAME OVER ===")
    else:
        print("Invalid choice.")
elif choice1 == "right":
    health -= 5
    print(f"Health: {health}")
    
    choice2 = input("Do you fight or run? ")
    if choice2 == "run":
        health -= 2
        print(f"Health: {health}")
        
        choice3 = input("Do you take or leave? ")
        if choice3 == "leave":
            print("=== GAME OVER ===")
        elif choice3 == "take":
            print("=== YOU WIN ===")
        else:
            print("Invalid choice.")
    elif choice2 == "fight":
        print("=== GAME OVER ===")
    else:
        print("Invalid choice.")

else:
    print("Invalid choice.")