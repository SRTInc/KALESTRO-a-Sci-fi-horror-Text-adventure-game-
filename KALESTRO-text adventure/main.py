#RESOURCES
"""
print(player_char.health)
    player_char.View_diary()
    #player_char.health = 0
    if player_char.health == 0:
        pc.dies('hi')
"""
import random
import time
import os

#classes
class pc:
    name = "Randal"
    age = 28
    occupation = "System Analyst"
    Current_objective = "Escape the KALESTRO geo-stationary space station"
    health = 100
    stamina = 100
    personal_details = [name,age,occupation,Current_objective]
    inventory = []
    def View_diary(self):
        for i in pc.personal_details:
            print(i)
    def dies(self):
        #health = 0
        print("YOU DIED!")
        print("Alas Your journey has ended")
player_char = pc()

#values
para1 = """In the far reaches of an unknown galaxy, 
The GRV megacorp. has colonised a barren planet and turned it into an mining colony
\n\"Helios-76\" ,a vast barren wasteland but yet it holds the coveted koplos crystals."""
para2 = """...After having a strange dream, you try to wake up from your bed. But your whole body is in pain.\n
You try your very best to get off the fricking bed.\n
Suddenly the SIRENS go off which...of course almost deafens your EARS.\n
You regained your senses.......\n\n
What will be your first course of action?(enter the number!)"""

cn1 = "The Awakening"

#modules
def display_intro():
        print("\n")
        for i in para1:
           #time.sleep(.031)
            print(i,end="")
        #print("\"Helios-76\" ,a vast barren wasteland but yet it holds the coveted keplos crystals.")
        print("")
        print("")
        print("")
def display_chapter1_text():
    for i in para2:
        #time.sleep(.031)
        print(i,end="")
    print('''\n1)Check out the window\n
2)Cover your ears and try to assess the current situaion\n
3)Go back to bed...\n''')
    while True:
        c = int(input())
        if c == 1:
            print("You rush towards the window and see the commotion thats happening below...you think to yourself\"No way\" as you realize there are some creatures running amok and viciously killing any hapless human in their way.\nThe bloody gore filled scenery almost makes you to vomit as you are filled with sheer disgust and...FEAR.Your hands are trembling and you tripped your foot and fell down all the while trying your best to get a hold of yourself shivering in terror!")
        elif c == 2:
            print("After covering your ears, you went to the door and wanted to ask the others what the hell is going on...\nBut the door is locked!...and you rush to check your PDA to see what's going on. Dread and panic is what you after seeing the newsfeed with videos of some strange horrifying creatures running amok and viciously killing any hapless human in their way.\nThe bloody gore filled scenery almost makes you to vomit as you are filled with sheer disgust and...FEAR.Your hands are trembling and you dropped your PDA all the while trying your best to get a hold of yourself shivering in terror! ")
        else:
            print("You try to get some sleep again...BUT ARE YOU SERIOUSLY OUT OF YOUR MIND?.ATLEAST ACKNOWLEGDE THERE ARE FUCKING SIRENS GOING OFF!(Something kills in your sleep)")
            player_char.dies()



if __name__=="__main__":
    display_intro()
    input("PRESS ANY KEY TO ENTER....")
    os.system('cls')
    print("\t CHAPTER I -",end="")
    for i in cn1: 
        #time.sleep(.031)
        print(i,end="")
    print("\n\n")
    display_chapter1_text()

    
    







