import customtkinter as ctk
import os
import json

with open("C:/Program Files/InfinityCalculator/settings.json") as file:
    

settings = ctk.CTk()
settings.title("Settings")
settings.geometry("400x400")

appearanceSelectionSegmentedButton.set(" System")
themeSelectionOptionMenu.set("Blue")
textColorSelectionOptionMenu.set("Black")

def changeAppearance(choice):
    if choice == " System":
        ctk.set_appearance_mode("system")
    elif choice == " Dark ":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

def changeTextColor(choice):
    if choice == "Red":
        print("red")
    elif choice == "Orange":
        print("orange")
    elif choice == "Yellow":
        print("yellow")
    elif choice == "Green":
        print("green")
    elif choice == "Cyan":
        print("cyan")
    elif choice == "Blue":
        print("blue")
    elif choice == "Dark Blue":
        print("dark blue")
    elif choice == "Purple":
        print("purple")
    elif choice == "Magenta":
        print("magenta")
    elif choice == "Pink":
        print("pink")
    elif choice == "Brown":
        print("brown")
    elif choice == "Black":
        print("black")

def changeTheme(choice):
    if choice == "Red":
        print("red")
    elif choice == "Orange":
        print("orange")
    elif choice == "Yellow":
        print("yellow")
    elif choice == "Green":
        ctk.set_default_color_theme("green")
    elif choice == "Cyan":
        print("cyan")
    elif choice == "Blue":
        ctk.set_default_color_theme("blue")
    elif choice == "Dark Blue":
        ctk.set_default_color_theme("dark-blue")
    elif choice == "Purple":
        print("purple")
    elif choice == "Magenta":
        print("magenta")
    elif choice == "Pink":
        print("pink")
    elif choice == "Brown":
        print("brown")
    elif choice == "Black":
        print("black")

appearanceSelectionDescriptionLabel = ctk.CTkLabel(settings, text=" Appearance Mode:   ")
appearanceSelectionDescriptionLabel.grid(row=0, column=0, sticky="w")

appearanceSelectionSegmentedButton = ctk.CTkSegmentedButton(settings, values=[" System", " Dark ", " Light "], command=changeAppearance, width=156)
appearanceSelectionSegmentedButton.grid(row=0, column=1)

iL = ctk.CTkLabel(settings, text="")
iL.grid(row=1, column=0)

themeSelectionDescriptionLabel = ctk.CTkLabel(settings, text=" Theme:             ")
themeSelectionDescriptionLabel.grid(row=2, column=0, sticky="w")

themeSelectionOptionMenu = ctk.CTkOptionMenu(settings, values=["Red", "Orange", "Yellow", "Green", "Cyan", "Blue", "Dark Blue", "Purple", "Magenta", "Pink", "Brown", "Black"], command=changeTheme, width=156)
themeSelectionOptionMenu.grid(row=2, column=1)

iLT = ctk.CTkLabel(settings, text="")
iLT.grid(row=3, column=0)

textColorSelectionDescriptionLabel = ctk.CTkLabel(settings, text=" Text Color:        ")
textColorSelectionDescriptionLabel.grid(row=4, column=0, sticky="w")

textColorSelectionOptionMenu = ctk.CTkOptionMenu(settings, values=["Red", "Orange", "Yellow", "Green", "Cyan", "Blue", "Dark Blue", "Purple", "Magenta", "Pink", "Brown", "Black"], command=changeTheme, width=156)
textColorSelectionOptionMenu.grid(row=4, column=1)

settings.mainloop()