import customtkinter as ctk
from PIL import Image, ImageTk
import io
import os

calculator = ctk.CTk()
calculator.title("Calculator")
calculator.geometry("497x700")

desktopPath = os.path.join(os.getenv('USERPROFILE'), 'Desktop')
onedrivePath = os.path.join(os.getenv('USERPROFILE'), 'OneDrive')
if os.path.exists(onedrivePath):
    desktopPath = os.path.join(onedrivePath, 'Desktop')

outputList = []

outputP1 = ctk.CTkLabel(calculator, text=outputList)
outputP1.grid(row=0, column=0, padx=6, pady=6)

outputP2 = ctk.CTkLabel(calculator, text=outputList)
outputP2.grid(row=1, column=0, padx=6, pady=6)

leftParenthesisButton = ctk.CTkButton(calculator, text="(", width=50, height=50)
leftParenthesisButton.grid(row=2, column=0, padx=6, pady=6)

rightParenthesisButton = ctk.CTkButton(calculator, text=")", width=50, height=50)
rightParenthesisButton.grid(row=2, column=1, padx=6, pady=6)

clearButton = ctk.CTkButton(calculator, text="Clear", width=50, height=50)
clearButton.grid(row=2, column=2, padx=6, pady=6)

backspaceButton = ctk.CTkButton(calculator, text="⌫", width=50, height=50)
backspaceButton.grid(row=2, column=3, padx=6, pady=6)

sevenButton = ctk.CTkButton(calculator, text="7", width=50, height=50)
sevenButton.grid(row=3, column=0, padx=6, pady=6)

eightButton = ctk.CTkButton(calculator, text="8", width=50, height=50)
eightButton.grid(row=3, column=1, padx=6, pady=6)

nineButton = ctk.CTkButton(calculator, text="9", width=50, height=50)
nineButton.grid(row=3, column=2, padx=6, pady=6)

divideButton = ctk.CTkButton(calculator, text="÷", width=50, height=50)
divideButton.grid(row=3, column=3, padx=6, pady=6)

fourButton = ctk.CTkButton(calculator, text="4", width=50, height=50)
fourButton.grid(row=4, column=0, padx=6, pady=6)

fiveButton = ctk.CTkButton(calculator, text="5", width=50, height=50)
fiveButton.grid(row=4, column=1, padx=6, pady=6)

sixButton = ctk.CTkButton(calculator, text="6", width=50, height=50)
sixButton.grid(row=4, column=2, padx=6, pady=6)

multiplyButton = ctk.CTkButton(calculator, text="×", width=50, height=50)
multiplyButton.grid(row=4, column=3, padx=6, pady=6)

oneButton = ctk.CTkButton(calculator, text="1", width=50, height=50)
oneButton.grid(row=5, column=0, padx=6, pady=6)

twoButton = ctk.CTkButton(calculator, text="2", width=50, height=50)
twoButton.grid(row=5, column=1, padx=6, pady=6)

threeButton = ctk.CTkButton(calculator, text="3", width=50, height=50)
threeButton.grid(row=5, column=2, padx=6, pady=6)

subtractButton = ctk.CTkButton(calculator, text="-", width=50, height=50)
subtractButton.grid(row=5, column=3, padx=6, pady=6)

oneButton = ctk.CTkButton(calculator, text="0", width=50, height=50)
oneButton.grid(row=6, column=0, padx=6, pady=6)

twoButton = ctk.CTkButton(calculator, text=".", width=50, height=50)
twoButton.grid(row=6, column=1, padx=6, pady=6)

threeButton = ctk.CTkButton(calculator, text="=", width=50, height=50)
threeButton.grid(row=6, column=2, padx=6, pady=6)

subtractButton = ctk.CTkButton(calculator, text="+", width=50, height=50)
subtractButton.grid(row=6, column=3, padx=6, pady=6)

xvarButton = ctk.CTkButton(calculator, text="𝑥", width=50, height=50, font=ctk.CTkFont(size=20))
xvarButton.grid(row=2, column=4, padx=6, pady=6)

yvarButton = ctk.CTkButton(calculator, text="𝑦", width=50, height=50, font=ctk.CTkFont(size=20))
yvarButton.grid(row=2, column=5, padx=6, pady=6)

ivarButton = ctk.CTkButton(calculator, text="𝑖", width=50, height=50, font=ctk.CTkFont(size=20))
ivarButton.grid(row=2, column=6, padx=6, pady=6)

percentageButton = ctk.CTkButton(calculator, text="%", width=50, height=50)
percentageButton.grid(row=2, column=7, padx=6, pady=6)

with open(desktopPath + "/InfinityCalculator/assets/button_images/exponent_white.png", "rb") as file:
    exponentData = file.read()

exponentSymbol = Image.open(io.BytesIO(exponentData))
exponentSymbol = ctk.CTkImage(light_image=exponentSymbol, dark_image=exponentSymbol, size=(25, 25))

exponentButton = ctk.CTkButton(calculator, text="", image=exponentSymbol, width=50, height=50)
exponentButton.grid(row=3, column=4, padx=6, pady=6)

squaredButton = ctk.CTkButton(calculator, text="□²", width=50, height=50)
squaredButton.grid(row=3, column=5, padx=6, pady=6)

absoluteValueBarsButton = ctk.CTkButton(calculator, text="|□|", width=50, height=50)
absoluteValueBarsButton.grid(row=3, column=6, padx=6, pady=6)

with open(desktopPath + "/InfinityCalculator/assets/button_images/mixed_fraction_white.png", "rb") as file:
    mixedFractionData = file.read()

mixedFractionSymbol = Image.open(io.BytesIO(mixedFractionData))
mixedFractionSymbol = ctk.CTkImage(light_image=mixedFractionSymbol, dark_image=mixedFractionSymbol, size=(25, 25))

mixedFractionButton = ctk.CTkButton(calculator, text="", image=mixedFractionSymbol, width=50, height=50)
mixedFractionButton.grid(row=3, column=7, padx=6, pady=6)

with open(desktopPath + "/InfinityCalculator/assets/button_images/fraction_white.png", "rb") as file:
    fractionData = file.read()

fractionSymbol = Image.open(io.BytesIO(fractionData))
fractionSymbol = ctk.CTkImage(light_image=fractionSymbol, dark_image=fractionSymbol, size=(25, 25))

fractionButton = ctk.CTkButton(calculator, text="", image=fractionSymbol, width=50, height=50)
fractionButton.grid(row=4, column=4, padx=6, pady=6)

factorialButton = ctk.CTkButton(calculator, text="□!", width=50, height=50)
factorialButton.grid(row=4, column=5, padx=6, pady=6)

with open(desktopPath + "/InfinityCalculator/assets/button_images/nth_root_white.png", "rb") as file:
    nthRootData = file.read()

nthRootSymbol = Image.open(io.BytesIO(nthRootData))
nthRootSymbol = ctk.CTkImage(light_image=nthRootSymbol, dark_image=nthRootSymbol, size=(25, 25))

nthRootButton = ctk.CTkButton(calculator, text="", image=nthRootSymbol, width=50, height=50)
nthRootButton.grid(row=4, column=6, padx=6, pady=6)

with open(desktopPath + "/InfinityCalculator/assets/button_images/square_root_white.png", "rb") as file:
    squareRootData = file.read()

squareRootSymbol = Image.open(io.BytesIO(squareRootData))
squareRootSymbol = ctk.CTkImage(light_image=squareRootSymbol, dark_image=squareRootSymbol, size=(25, 25))

squareRootButton = ctk.CTkButton(calculator, text="", image=squareRootSymbol, width=50, height=50)
squareRootButton.grid(row=4, column=7, padx=6, pady=6)

lessThanEqualTo = ctk.CTkButton(calculator, text="≤", width=50, height=50)
lessThanEqualTo.grid(row=5, column=4, padx=6, pady=6)

greaterThanEqualTo = ctk.CTkButton(calculator, text="≥", width=50, height=50)
greaterThanEqualTo.grid(row=5, column=5, padx=6, pady=6)

lessThan = ctk.CTkButton(calculator, text="<", width=50, height=50)
lessThan.grid(row=5, column=6, padx=6, pady=6)

moreThan = ctk.CTkButton(calculator, text=">", width=50, height=50)
moreThan.grid(row=5, column=7, padx=6, pady=6)

thetaButton = ctk.CTkButton(calculator, text="θ", width=50, height=50)
thetaButton.grid(row=6, column=4, padx=6, pady=6)

piButton = ctk.CTkButton(calculator, text="π", width=50, height=50)
piButton.grid(row=6, column=5, padx=6, pady=6)

tauButton = ctk.CTkButton(calculator, text="τ", width=50, height=50)
tauButton.grid(row=6, column=6, padx=6, pady=6)

commaButton = ctk.CTkButton(calculator, text=",", width=50, height=50)
commaButton.grid(row=6, column=7, padx=6, pady=6)

sinButton = ctk.CTkButton(calculator, text="sin", width=50, height=50)
sinButton.grid(row=7, column=0, padx=6, pady=6)

cscButton = ctk.CTkButton(calculator, text="csc", width=50, height=50)
cscButton.grid(row=7, column=1, padx=6, pady=6)

sinhButton = ctk.CTkButton(calculator, text="sinh", width=50, height=50)
sinhButton.grid(row=7, column=2, padx=6, pady=6)

arcsinButton = ctk.CTkButton(calculator, text="arcsin", width=50, height=50)
arcsinButton.grid(row=7, column=3, padx=6, pady=6)

cosButton = ctk.CTkButton(calculator, text="cos", width=50, height=50)
cosButton.grid(row=7, column=4, padx=6, pady=6)

secButton = ctk.CTkButton(calculator, text="sec", width=50, height=50)
secButton.grid(row=7, column=5, padx=6, pady=6)

sechButton = ctk.CTkButton(calculator, text="sech", width=50, height=50)
sechButton.grid(row=7, column=6, padx=6, pady=6)

arccosButton = ctk.CTkButton(calculator, text="arccos", width=50, height=50)
arccosButton.grid(row=7, column=7, padx=6, pady=6)

tanButton = ctk.CTkButton(calculator, text="tan", width=50, height=50)
tanButton.grid(row=8, column=0, padx=6, pady=6)

cotButton = ctk.CTkButton(calculator, text="cot", width=50, height=50)
cotButton.grid(row=8, column=1, padx=6, pady=6)

tanhButton = ctk.CTkButton(calculator, text="tanh", width=50, height=50)
tanhButton.grid(row=8, column=2, padx=6, pady=6)

arctanButton = ctk.CTkButton(calculator, text="arctan", width=50, height=50)
arctanButton.grid(row=8, column=3, padx=6, pady=6)

with open(desktopPath + "/InfinityCalculator/assets/button_images/eulers_number_exponent_white.png", "rb") as file:
    eulersNumberExponentData = file.read()

eulersNumberExponentSymbol = Image.open(io.BytesIO(eulersNumberExponentData))
eulersNumberExponentSymbol = ctk.CTkImage(light_image=eulersNumberExponentSymbol, dark_image=eulersNumberExponentSymbol, size=(25, 25))

eulersNumberExponentButton = ctk.CTkButton(calculator, text="", image=eulersNumberExponentSymbol, width=50, height=50)
eulersNumberExponentButton.grid(row=8, column=4, padx=6, pady=6)

with open(desktopPath + "/InfinityCalculator/assets/button_images/eulers_number_white.png", "rb") as file:
    eulersNumberData = file.read()

eulersNumberSymbol = Image.open(io.BytesIO(eulersNumberData))
eulersNumberSymbol = ctk.CTkImage(light_image=eulersNumberSymbol, dark_image=eulersNumberSymbol, size=(25, 25))

eulersNumberButton = ctk.CTkButton(calculator, text="", image=eulersNumberSymbol, width=50, height=50)
eulersNumberButton.grid(row=8, column=5, padx=6, pady=6)

with open(desktopPath + "/InfinityCalculator/assets/button_images/settings.png", "rb") as file:
    settingsData = file.read()

settingsSymbol = Image.open(io.BytesIO(settingsData))
settingsSymbol = ctk.CTkImage(light_image=settingsSymbol, dark_image=settingsSymbol, size=(25, 25))

settingsButton = ctk.CTkButton(calculator, text="", image=settingsSymbol, width=50, height=50)
settingsButton.grid(row=8, column=6, padx=6, pady=6)

calculator.mainloop()
