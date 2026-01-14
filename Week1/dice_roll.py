import random
dice_art = {1: ("|￣￣￣￣￣￣￣￣|", 
                "|               |", 
                "|      ●        |", 
                "|               |", 
                "|               |", 
                "|_______________|"),
            2: ("|￣￣￣￣￣￣￣￣|", 
                "|   ●           |", 
                "|               |", 
                "|               |", 
                "|            ●  |", 
                "|_______________|"),
            3: ("|￣￣￣￣￣￣￣￣|", 
                "|   ●           |", 
                "|               |", 
                "|       ●       |", 
                "|             ● |", 
                "|_______________|"),
            4: ("|￣￣￣￣￣￣￣￣|", 
                "|   ●         ● |", 
                "|               |", 
                "|               |", 
                "|   ●         ● |", 
                "|_______________|"),
            5: ("|￣￣￣￣￣￣￣￣|", 
                "|   ●        ●  |", 
                "|               |", 
                "|       ●       |", 
                "|   ●         ● |", 
                "|_______________|"),
            6: ("|￣￣￣￣￣￣￣￣|", 
                "|               |", 
                "|   ●      ●    |", 
                "|   ●      ●    |", 
                "|   ●      ●    |", 
                "|_______________|")}

dice_num = []
dice = int(input("How many dice? "))
total = 0

for i in range(1, dice+1):
    dice_num.append(random.randint(1, 6))

for line in range(6):
    for die in dice_num:
        print(dice_art.get(die)[line], end=" ")
    print()

for dice in dice_num:
    total += dice
print(f"Total is: {total}")
