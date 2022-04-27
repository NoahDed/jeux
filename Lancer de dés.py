from random import randint
from tkinter import Y

repeat_rolling = True

while repeat_rolling:

    print("Vous avez obtenu le nombre suivant en utilisant le dé -",randint(1,6))
    print("Voulez-vous relancer les dés ?")
    
    repeat_rolling = ("y" or "yes") in input().lower()