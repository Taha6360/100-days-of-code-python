print(r'''
____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
first=input("at cross road , where u want to go \"left\" or \"right\"")
if first == "left":
    second=input("u have safely crossed there is a river to cross you will 'wait' or 'swim' ?")
    if second == "wait" :
       third = input ("you got 3 doors which one u will choose to go 'blue' or 'yellow' or 'red")
       if  third == "red":
           print("Burnt by fire game over")
       elif third == "blue":
           print("AHHhh beast u died game over!")
       elif third == "yellow":
           print("congrats u win")
       else:
           print("Game over")
    else:
        print("attacked by trout Game Over")

else:
    print("You have falled into hole GAME OVER")

