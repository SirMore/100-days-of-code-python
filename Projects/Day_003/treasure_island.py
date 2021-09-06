
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
********************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Which direction do you wanna go?
direction = input("You are at a crossroad. Which direction do you want to go? Type 'left' or 'right'\n")
direct_lower = direction.lower()

if direction == "left":

    # Which action do you want to take
    transport = input("You've arrived at a lake. There's an island in the middle of this lake.\nType 'swim' to swim across or type 'wait' to wait for a boat which comes every 45 mins.\n")
    transport_lower = transport.lower()
    if transport_lower == "wait":

        #Which door to Enter
        door = input("You arrive on the island. There is a house with 3 doors. One red, one yellow and one blue.\nWhich one would you choose to enter?\n")
        door_lower = door.lower()
        if door_lower == "yellow": 
            print("Oh Great! You've found Blackbeard's Treasure. You win!")
        elif door_lower == 'red' or door_lower == 'blue': 
            print("Oh no! You've been captured by Blackbeard and his crew. Game Over!")
        else:
            print("Wrong choice! Try the game again.")
    
    elif transport_lower == "swim":
        print("Oh no! You've been eaten by a huge crocodile. Game over!")
    else:
        print("Wrong choice! Try playing the game again.")

else:
    print("Oh no!! You've fallen into a hidden hole. Game over!")
