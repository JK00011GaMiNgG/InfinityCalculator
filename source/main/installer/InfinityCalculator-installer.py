import tkinter as tk
from PIL import Image, ImageTk
from tkhtmlview import HTMLLabel
import requests
import os
import winshell
from win32com.client import Dispatch

if not os.path.exists("C:/Program Files/InfinityCalculator"):
    desktopPath = os.path.join(os.getenv('USERPROFILE'), 'Desktop')
    onedrivePath = os.path.join(os.getenv('USERPROFILE'), 'OneDrive')
    if os.path.exists(onedrivePath):
        desktopPath = os.path.join(onedrivePath, 'Desktop')

    fontFamily = "Segoe UI"
    fontSize = 12
    linkFontSize = 10

    def createShortcut(path, target='', wDir='', icon=''):    
        ext = path[-3:]
        if ext == 'url':
            shortcut = file(path, 'w')
            shortcut.write('[InternetShortcut]\n')
            shortcut.write('URL=%s' % target)
            shortcut.close()
        else:
            shell = Dispatch('WScript.Shell')
            shortcut = shell.CreateShortCut(path)
            shortcut.Targetpath = target
            shortcut.WorkingDirectory = wDir
            if icon == '':
                pass
            else:
                shortcut.IconLocation = icon
            shortcut.save()

    def downloadFile(url, fileName, downloadDirectory):
        os.makedirs(downloadDirectory, exist_ok=True)
        filePath = os.path.join(downloadDirectory, fileName)
        response = requests.get(url)
        if response.status_code == 200:
            with open(filePath, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download file from {url}. Status code: {response.status_code}")

    def centerWindow(window, width, height):
        screenWidth = window.winfo_screenwidth()
        screenHeight = window.winfo_screenheight()
        x = (screenWidth - width) // 2
        y = (screenHeight - height) // 2
        window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def secondTab(hasRequirements=None):
        def back():
            secondTabOfInstaller.destroy()
            firstTab(hasRequirements.get())

        global isGoingToCreateDesktopShortcut
        global isGoingToCreateStartMenuShortcut
        global isGoingToLaunchAfterInstallation
        isGoingToCreateDesktopShortcut = False
        isGoingToCreateStartMenuShortcut = False
        isGoingToLaunchAfterInstallation = False

        def checkDesktopShortcut():
            if createDesktopShortcutVar.get() == "oh hell yeah":
                isGoingToCreateDesktopShortcut = True
            elif createDesktopShortcutVar.get() == "oh hell no":
                isGoingToCreateDesktopShortcut = False

        def checkStartMenuShortcut():
            if createStartMenuShortcutVar.get() == "yep":
                isGoingToCreateStartMenuShortcut = True
            elif createStartMenuShortcutVar.get() == "nope":
                isGoingToCreateStartMenuShortcut = False

        def checkLaunchAfterInstallation():
            if launchAfterInstallationVar.get() == "on":
                isGoingToLaunchAfterInstallation = True
            elif launchAfterInstallationVar.get() == "off":
                isGoingToLaunchAfterInstallation = False

        secondTabOfInstaller = tk.Tk()
        secondTabOfInstaller.title("Infinity Calculator Installer (2 of 2)")

        createDesktopShortcutVar = tk.StringVar(value="oh hell no")
        createDesktopShortcut = tk.Checkbutton(secondTabOfInstaller, text="Create Shortcut On Desktop", command=checkDesktopShortcut, variable=createDesktopShortcutVar, onvalue="oh hell yeah", offvalue="oh hell no")
        createDesktopShortcut.grid(row=0, column=0, sticky="w")

        createStartMenuShortcutVar = tk.StringVar(value="nope")
        createStartMenuShortcut = tk.Checkbutton(secondTabOfInstaller, text="Create Shortcut On The Start Menu", command=checkStartMenuShortcut, variable=createStartMenuShortcutVar, onvalue="yep", offvalue="nope")
        createStartMenuShortcut.grid(row=2, column=0, sticky="w")

        launchAfterInstallationVar = tk.StringVar(value="off")
        launchAfterInstallation = tk.Checkbutton(secondTabOfInstaller, text="Launch Program After Installation", command=checkLaunchAfterInstallation, variable=launchAfterInstallationVar, onvalue="on", offvalue="off")
        launchAfterInstallation.grid(row=4, column=0, sticky="w")

        iL = tk.Label(secondTabOfInstaller, text="")
        iL.grid(row=1, column=0)

        iLTH = tk.Label(secondTabOfInstaller, text="")
        iLTH.grid(row=3, column=0)

        iLF = tk.Label(secondTabOfInstaller, text="")
        iLF.grid(row=5, column=0)

        iLFI = tk.Label(secondTabOfInstaller, text="")
        iLFI.grid(row=6, column=0)

        checkStartMenuShortcut()
        checkDesktopShortcut()
        checkLaunchAfterInstallation()

        def install():
            secondTabOfInstaller.destroy()
            thirdTab()

        finishButton = tk.Button(secondTabOfInstaller, text="Finish", command=install, width=10)
        finishButton.grid(row=7, column=1, sticky="e")

        backButton = tk.Button(secondTabOfInstaller, text="Back", command=back, width=10)
        backButton.grid(row=7, column=0, sticky="w", padx=40)

        windowWidth = 360
        windowHeight = 200

        centerWindow(secondTabOfInstaller, windowWidth, windowHeight)
        secondTabOfInstaller.mainloop()

    def firstTab(initialState=None):
        def enableNextButton():
            nextButton.config(state='active')

        def switchTabs():
            firstTabOfInstaller.destroy()
            secondTab(hasRequirements)

        firstTabOfInstaller = tk.Tk()
        firstTabOfInstaller.title("Infinity Calculator Installer (1 of 2)")

        requirements = """
        Requirements To Run the program:

        • Python 3.10 or later (Only tested on 3.10-3.13)           

        • Windows 7-11 (Not supported on Mac or Linux YET)

        • (Disabled) JRE 17 or later                                                 
        """
        nextButton = tk.Button(firstTabOfInstaller, text="Next", state='disabled', command=switchTabs, width=10)
        nextButton.grid(row=2, column=0, sticky="e")

        if initialState is not None:
            nextButton.config(state='active')

        requirementsLabel = tk.Label(firstTabOfInstaller, text=requirements)
        requirementsLabel.grid(row=0, column=0, sticky="w")

        hasRequirements = tk.BooleanVar(value=initialState) if initialState is not None else tk.BooleanVar(value=False)

        hasAllRequirementsCheckbox = tk.Checkbutton(firstTabOfInstaller, text="Done installing the requirements or already have them.", command=enableNextButton, variable=hasRequirements)
        hasAllRequirementsCheckbox.grid(row=1, column=0, sticky="w")

        cancelButton = tk.Button(firstTabOfInstaller, text="Cancel", state='active', command=lambda:firstTabOfInstaller.destroy(), width=10)
        cancelButton.grid(row=2, column=0, sticky="w", padx=40)

        windowWidth = 360
        windowHeight = 200

        centerWindow(firstTabOfInstaller, windowWidth, windowHeight)
        firstTabOfInstaller.mainloop()

    def fourthTab():
        fourthTabOfInstaller = tk.Tk()
        fourthTabOfInstaller.title("Infinity Calculator Installer")

        sourceCodeLink = HTMLLabel(fourthTabOfInstaller, html='<a style="font-size: {}px;" href="https://github.com/JK00011GaMiNgG/InfinityCalculator"> github.com/JK00011GaMiNgG/InfinityCalculator </a>'.format(linkFontSize), font=(fontFamily, fontSize))
        bugReportLink = HTMLLabel(fourthTabOfInstaller, html='<a style="font-size: {}px;" href="https://github.com/JK00011GaMiNgG/InfinityCalculator/issues"> github.com/JK00011GaMiNgG/InfinityCalculator/issues </a>'.format(linkFontSize), font=(fontFamily, fontSize))
        updatesLink = HTMLLabel(fourthTabOfInstaller, html='<a style="font-size: {}px;" href="https://github.com/JK00011GaMiNgG/InfinityCalculator/releases"> github.com/JK00011GaMiNgG/InfinityCalculator/releases </a>'.format(linkFontSize), font=(fontFamily, fontSize))
        helpLink = HTMLLabel(fourthTabOfInstaller, html='<a style="font-size: {}px;" href="https://github.com/JK00011GaMiNgG/InfinityCalculator/issues"> github.com/JK00011GaMiNgG/InfinityCalculator/issues </a>'.format(linkFontSize), font=(fontFamily, fontSize))
        sourceCodeLabel = tk.Label(fourthTabOfInstaller, text="Source Code:")
        bugReportLabel = tk.Label(fourthTabOfInstaller, text="Bug Report:")
        updatesLabel = tk.Label(fourthTabOfInstaller, text="Updates:")
        helpLabel = tk.Label(fourthTabOfInstaller, text="Help:")

        sourceCodeLabel.place(x=0, y=20)
        sourceCodeLink.place(x=0, y=30)
        bugReportLabel.place(x=0, y=55)
        bugReportLink.place(x=0, y=65)
        updatesLabel.place(x=0, y=90)
        updatesLink.place(x=0, y=100)
        helpLabel.place(x=0, y=125)
        helpLink.place(x=0, y=135)

        successfullyInstalledLabel = tk.Label(fourthTabOfInstaller, text="Successfully Installed Infinity Calculator.")
        successfullyInstalledLabel.grid(row=0, column=0, sticky="w")

        closeButton = tk.Button(fourthTabOfInstaller, text="Close", width=10, command=lambda: fourthTabOfInstaller.destroy())
        closeButton.place(x=130, y=170)

        windowWidth = 360
        windowHeight = 200

        centerWindow(fourthTabOfInstaller, windowWidth, windowHeight)
        fourthTabOfInstaller.mainloop()

    def thirdTab():
        def switchTabs():
            thirdTabOfInstaller.destroy()
            fourthTab()

        thirdTabOfInstaller = tk.Tk()
        thirdTabOfInstaller.title("Infinity Calculator Installer (2 of 2)")
        windowWidth = 360
        windowHeight = 200

        iL = tk.Label(thirdTabOfInstaller, text="            ")
        iL.grid(row=0, column=0)

        installingLabel = tk.Label(thirdTabOfInstaller, text="Installing...")
        installingLabel.grid(row=0, column=1)

        animationLabel = tk.Label(thirdTabOfInstaller)
        animationLabel.grid(row=1, column=1)

        iLT = tk.Label(thirdTabOfInstaller, text="")
        iLT.grid(row=2, column=1)

        iLTH = tk.Label(thirdTabOfInstaller, text="")
        iLTH.grid(row=3, column=1)

        iLF = tk.Label(thirdTabOfInstaller, text="")
        iLF.grid(row=4, column=1)

        iLFI = tk.Label(thirdTabOfInstaller, text="")
        iLFI.grid(row=5, column=1)

        iLS = tk.Label(thirdTabOfInstaller, text="")
        iLS.grid(row=6, column=1)

        iLSE = tk.Label(thirdTabOfInstaller, text="")
        iLSE.grid(row=7, column=1)

        cancelButton = tk.Button(thirdTabOfInstaller, text="Cancel", state='active', command=lambda:thirdTabOfInstaller.destroy(), width=10)
        cancelButton.grid(row=8, column=1, sticky="w")

        def updateAnimation(frameNumber):
            if frameNumber > 15:
                frameNumber = 15

            framePath = os.path.join(desktopPath, "InfinityCalculator", "source", "main", "installer", "frames", f"{frameNumber}.png")
            frame = Image.open(framePath)

            originalWidth, originalHeight = frame.size
            newWidth = originalWidth * 2
            newHeight = originalHeight * 2
            resizedImage = frame.resize((newWidth, newHeight))

            frameImage = ImageTk.PhotoImage(resizedImage)

            animationLabel.configure(image=frameImage)
            animationLabel.image = frameImage

            if frameNumber < 15:
                thirdTabOfInstaller.after(100, updateAnimation, frameNumber + 1)
            else:
                installFiles()

        def installFiles():
            switchTabs()
            os.makedirs("C:/Program Files/InfinityCalculator/assets/button_images/", exist_ok=False)
            os.makedirs("C:/Program Files/InfinityCalculator/assets/icons/", exist_ok=False)
            os.makedirs("C:/Program Files/InfinityCalculator/assets/themes/", exist_ok=False)
            os.makedirs("C:/Program Files/InfinityCalculator/python/addition/", exist_ok=False)
            os.makedirs("C:/Program Files/InfinityCalculator/python/subtraction/", exist_ok=False)
            os.makedirs("C:/Program Files/InfinityCalculator/python/multiplication/", exist_ok=False)
            os.makedirs("C:/Program Files/InfinityCalculator/python/division/", exist_ok=False)
            os.makedirs("C:/Program Files/InfinityCalculator/python/square_root/", exist_ok=False)
            downloadFile(
                "https://raw.githubusercontent.com/JK00011GaMiNgG/InfinityCalculator/main/source/main/python/calculator.py", 
                "calculator.py", 
                "C:/Program Files/InfinityCalculator/python"
            )
            downloadFile(
                "https://raw.githubusercontent.com/JK00011GaMiNgG/InfinityCalculator/assets/icons/icon.ico", 
                "icon.ico", 
                "C:/Program Files/InfinityCalculator/assets/icons/"
            )
            if isGoingToCreateDesktopShortcut == True:
                createShortcut(desktopPath, "C:/Program Files/InfinityCalculator/python/calculator.py", "C:/Program Files/InfinityCalculator/python/calculator.py", "C:/Program Files/InfinityCalculator/assets/icons/icon.ico")
            
        updateAnimation(0)

        centerWindow(thirdTabOfInstaller, windowWidth, windowHeight)
        thirdTabOfInstaller.mainloop()
    firstTab()

elif os.path.exists("C:/Program Files/InfinityCalculator"):
    alreadyInstalled = tk.Tk()
    alreadyInstalled.title("Already Installed Infinity Calculator")
    alreadyInstalled.geometry("200x100")

    alreadyInstalledLabel = tk.Label(alreadyInstalled, text="\nYou already have Infinity Calculator \nInstalled on this device!")
    alreadyInstalledLabel.place(x=3, y=10)

    okButton = tk.Button(alreadyInstalled, text="Ok", command=lambda: alreadyInstalled.destroy(), width=10)
    okButton.place(x=60, y=70)

    alreadyInstalled.mainloop()