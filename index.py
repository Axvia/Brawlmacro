from ReadWriteMemory import ReadWriteMemory
import os
import sys
import json
import tkinter as tk  
from tkinter import Label, Entry, StringVar, ttk, filedialog, PhotoImage, Canvas
from weapons import sword, hammer, blaster, lance, spear, katars, axe, bow, gauntlet, scythe, cannon, orb, greatsword
from assets import info, dev

# Generate json file upon start
if os.path.exists(os.getcwd() + '/keybinds.json'):
    # if json file exist, read it!
    with open("./keybinds.json") as f:
        keybindData = json.load(f)
else:
    # if json file not exist, create new one with this template
    configTemplate = { 
        "Key Up": "Up",
        "Key Down": "Down",
        "Key Right": "Right",
        "Key Left": "Left",
        "Key Jump": "Space",
        "Key Dodge": "z",
        "Key Light Attack": "c",
        "Key Heavy Attack": "x",
        "Key Throw": "v",
        "Key Pickup": "v",
        "Developer": {
            "Copyright":"Necode",
            "YouTube":"https://www.youtube.com/channel/UCn_48Cl9BjKKjvS3ADk1Ltw"
        }
    }
    # write the template
    with open (os.getcwd() + '/keybinds.json', 'w+') as f:
        json.dump(configTemplate, f, indent=4, sort_keys=False)

# Provide relative path to packed file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
# End

# Entry with Placeholder
class EntryWithPlaceholder(Entry):
    def __init__(self, *args, **kwargs):
        self.placeholder = kwargs.pop("placeholder", "")
        super().__init__(*args, **kwargs)
        self.insert("end", self.placeholder)
        self.bind("<FocusIn>", self.remove_placeholder)
        self.bind("<FocusOut>", self.add_placeholder)
    def remove_placeholder(self, event):
        if self.get() == self.placeholder:
            self.delete(0, "end")

    def add_placeholder(self,event):
        if self.placeholder and self.get() == "":
            self.insert(0, self.placeholder)
# End

# Create window
app = tk.Tk()
app.resizable(width=False, height=False)
app.iconbitmap(resource_path('icon/app.ico'))
app.title("Advnecode")
# End

# Margin 1
appMarg = tk.LabelFrame(app, text="Weapons", padx=5, pady=5)
appMarg.pack(padx=5, pady=5)
# End

# Weapon Sword
SwordPrev = PhotoImage(file=resource_path("images/Sword_Icon.png"))
WeapSword = tk.Button(appMarg, image=SwordPrev, compound="center", command=sword.OpenApp) #, text="Sword")
WeapSword.grid(row=1,column=1)
# End

# Weapon Hammer
HammPrev = PhotoImage(file=resource_path("images/Hammer_Icon.png"))
WeapHamm = tk.Button(appMarg, image=HammPrev, compound="center", command=hammer.OpenApp) #, text="Hammer")
WeapHamm.grid(row=1, column=2)
# End

# Weapon Blaster
BlstPrev = PhotoImage(file=resource_path("images/Blasters_Icon.png"))
WeapBlst = tk.Button(appMarg, image=BlstPrev, compound="center", command=blaster.OpenApp) #, text="Blaster")
WeapBlst.grid(row=1, column=3)
# End

# Weapon Lance
LancPrev = PhotoImage(file=resource_path("images/Lance_Icon.png"))
WeapLanc = tk.Button(appMarg, image=LancPrev, compound="center", command=lance.OpenApp) #, text="Lance")
WeapLanc.grid(row=2, column=1)
# End

# Weapon Spear
SperPrev = PhotoImage(file=resource_path("images/Spear_Icon.png"))
WeapSper = tk.Button(appMarg, image=SperPrev, compound="center", command=spear.OpenApp) #, text="Spear")
WeapSper.grid(row=2, column=2)
# End

# Weapon Katars
KatrPrev = PhotoImage(file=resource_path("images/Katars_Icon.png"))
WeapKatr = tk.Button(appMarg, image=KatrPrev, compound="center", command=katars.OpenApp) #, text="Katars")
WeapKatr.grid(row=2, column=3)
# End

# Weapon Axe
AxesPrev = PhotoImage(file=resource_path("images/Axe_Icon.png"))
WeapAxes = tk.Button(appMarg, image=AxesPrev, compound="center", command=axe.OpenApp) #, text="Axe")
WeapAxes.grid(row=3, column=1)
# End

# Weapon Bow
BowsPrev = PhotoImage(file=resource_path("images/Bow_Icon.png"))
WeapBows = tk.Button(appMarg, image=BowsPrev, compound="center", command=bow.OpenApp) #, text="Bow")
WeapBows.grid(row=3, column=2)
# End

# Weapon Gauntlet
GnltPrev = PhotoImage(file=resource_path("images/Gauntlets_Icon.png"))
WeapGnlt = tk.Button(appMarg, image=GnltPrev, compound="center", command=gauntlet.OpenApp) #, text="Gauntlet")
WeapGnlt.grid(row=3, column=3)
# End

# Weapon Scythe
ScytPrev = PhotoImage(file=resource_path("images/Scythe_Icon.png"))
WeapScyt = tk.Button(appMarg, image=ScytPrev, compound="center", command=scythe.OpenApp) #, text="Scythe")
WeapScyt.grid(row=4, column=1)
# End

# Weapon Cannon
CannPrev = PhotoImage(file=resource_path("images/Cannon_Icon.png"))
WeapCann = tk.Button(appMarg, image=CannPrev, compound="center", command=cannon.OpenApp) #, text="Cannon")
WeapCann.grid(row=4, column=2)
# End

# Weapon Orb
OrbsPrev = PhotoImage(file=resource_path("images/Orb_Icon.png"))
WeapOrbs = tk.Button(appMarg, image=OrbsPrev, compound="center", command=orb.OpenApp) #, text="Orb")
WeapOrbs.grid(row=4, column=3)
# End

# Developer Logo
Avnecode = PhotoImage(file=resource_path("images/Necode.png"))
Avnecbtn = tk.Button(appMarg, image=Avnecode, compound="center", command=dev.App) #, text="Necode")
Avnecbtn.grid(row=5, column=1)
# End

# Weapon Greatsword
GrsdPrev = PhotoImage(file=resource_path("images/Greatsword_Icon.png"))
WeapGrsd = tk.Button(appMarg, image=GrsdPrev, compound="center", command=greatsword.OpenApp) #, text="Greatsword")
WeapGrsd.grid(row=5, column=2)
# End

# Info
InfoPrev = PhotoImage(file=resource_path("images/Info.png"))
InfoBttn = tk.Button(appMarg, image=InfoPrev, compound="center", command=info.App) #, text="Necode")
InfoBttn.grid(row=5, column=3)
# End



# Keep the window open
app.mainloop()
# End