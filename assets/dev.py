import tkinter as tk
from tkinter import ttk, HORIZONTAL, Label, Entry, StringVar
import os
import sys
import webbrowser
import time
from ReadWriteMemory import ReadWriteMemory
import keyboard
import json

# Provide relative path to packed file
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
# End

# Placeholder
class EntryWithPlaceholder(Entry):
	def __init__(self, *args, **kwargs):
		self.placeholder = kwargs.pop("placeholder", "")
		super().__init__(*args, **kwargs)

		self.insert("end", self.placeholder)
		self.bind("<FocusIn>", self.remove_placeholder)
		self.bind("<FocusOut>", self.add_placeholder)

	def remove_placeholder(self, event):
		"""Remove placeholder text, if present"""
		if self.get() == self.placeholder:
			self.delete(0, "end")

	def add_placeholder(self,event):
		"""Add placeholder text if the widget is empty"""
		if self.placeholder and self.get() == "":
			self.insert(0, self.placeholder)
# End

def App():
	# Window
	app = tk.Toplevel()
	app.title("Developer")
	app.resizable(width=False, height=False)
	app.iconbitmap(resource_path('icon/app.ico'))
	# End

	# Margin 2
	appMarg2 = tk.LabelFrame(app, text="Software Usage", padx=5, pady=5)
	appMarg2.pack(padx=5, pady=5)
	# End

	# Label Usage
	Usages = """1. To avoid uncontrollable key please don't hold the key over 2 seconds.
2. Don't pick the key that already used.
3. Uppercase key (D) Lowercase (d) key are different input.
4. Some of combo require to press left or right manually"""
	LblUsgs = tk.Label(appMarg2, text=Usages)
	LblUsgs.grid(row=1, column=1)

	# Margin 2
	appMarg3 = tk.LabelFrame(app, text="Readme", padx=5, pady=5)
	appMarg3.pack(padx=5, pady=5)
	# End

	# Label Readme
	Notes = """1. Software can't do anything automated like bot.
2. Developer of this software can't make bot.
3. Software can't manipulate program memory.
4. Software not compatile with 32-bit Operating System.
5. Any feedback asking to make bot will lead you to instant banned.
6. Delete the software if you think this is a virus.
7. Pro Gamer don't need this macro.
8. Use this software just for fun.
9. Use this software at your own risk.
10. Software only doing short combo.
11. Using this software is not allowed by game developer.
12. Software can't always give you true combo.
13. Software only work on windows.
14. Success rate for true combo depend on dexterity"""
	LblUsgs1 = tk.Label(appMarg3, text=Notes)
	LblUsgs1.grid(row=1, column=1)
	# End

	# Anime Server
	def AnimeUrl():
		OpenBtn1['state'] = "disabled"
		webbrowser.open_new("https://discord.gg/mpwhJkN5VW")
		OpenBtn1['state'] = "enable"

	# Programmer Server
	def ProgUrl():
		OpenBtn2['state'] = "disabled"
		webbrowser.open_new("https://discord.gg/URCNH7KW4Q")
		OpenBtn2['state'] = "enable"

	# Youtube Channel
	def YouTubeChannel():
		LblYTOpn['state'] = "disabled"
		webbrowser.open_new("https://www.youtube.com/channel/UCn_48Cl9BjKKjvS3ADk1Ltw")
		LblYTOpn['state'] = "enable"

	# Delete
	def deleteApp():
		sys.exit(1)

	# Margin 1
	appMarg = tk.LabelFrame(app, padx=5, pady=5)
	appMarg.pack(padx=5, pady=5)
	# End

	# Anime
	OpenBtn1 = ttk.Button(appMarg, text="Anime", command=AnimeUrl)
	OpenBtn1.grid(row=1,column=1)
	# End

	# Anime
	OpenBtn2 = ttk.Button(appMarg, text="Programmer", command=ProgUrl)
	OpenBtn2.grid(row=1,column=2)
	# End

	# Youtube
	LblYTOpn = ttk.Button(appMarg, text="YouTube", command=YouTubeChannel)
	LblYTOpn.grid(row=2, column=1)
	# End

	# Old Macro
	def sayDevName():
		win = tk.Toplevel()

		winMarg = tk.LabelFrame(win, text="Choosen Combo", padx=5, pady=5)
		winMarg.pack(padx=5, pady=5)

		LabelLogin = tk.Label(winMarg, text="Sign in:")
		LabelLogin.grid(row=1, column=1)

		LabelEntryText = StringVar(None)
		LabelEntry = EntryWithPlaceholder(winMarg, width=30, placeholder="Please enter developer name!", textvariable=LabelEntryText)
		LabelEntry.grid(row=1, column=2)

		# Login
		def onLogin():
			devName = LabelEntryText.get()
			if devName == "Necode" or devName == "necode" or devName == "NECODE":
				print("Correct")
				win.destroy()
				oldMacro()
			else:
				print("Incorrect")
				pass
		# End

		ButtonLogin = ttk.Button(winMarg, text="Login", command=onLogin)
		ButtonLogin.grid(row=1, column=3)

		win.after(1000, win.resizable(False, False))
		win.mainloop()
	
	LblExitOpn = ttk.Button(appMarg, text="Macro", command=sayDevName)
	LblExitOpn.grid(row=2, column=2)
	# End

	# Exit
	LblExitOpn = ttk.Button(app, text="Exit", command=deleteApp)
	LblExitOpn.pack(side="bottom")
	# End

	app.mainloop()


def oldMacro():
	# Read JSON file
	try:
		if os.path.exists(os.getcwd() + '/keybinds.json'):
			# if json file exist, read it!
			with open("./keybinds.json") as f:
				keybindData = json.load(f)
		# Read
		UP = keybindData["Key Up"]
		DOWN = keybindData["Key Down"]
		RIGHT = keybindData["Key Right"]
		LEFT = keybindData["Key Left"]
		JUMP = keybindData["Key Jump"]
		DODGE = keybindData["Key Dodge"]
		LightAttack = keybindData["Key Light Attack"]
		HeavyAttack = keybindData["Key Heavy Attack"]
	except Exception:
		print("keybinds.json not found. Generate new one!")

	# Check if the gameis running
	rwm = ReadWriteMemory()
	try:
		process = rwm.get_process_by_name("Brawlhalla.exe")
		process.open()
	except:
		root = tk.Toplevel()
		root.iconbitmap(resource_path('icon/app.ico'))
		root.title("Warning")
		notice = ttk.Label(root, text="Game not detected", width=30)
		notice.grid(row=1, column=1)
		def closeWarn():
			root.destroy()
		buttonClose = ttk.Button(root, text="Close", command=closeWarn)
		buttonClose.grid(row=1, column=2)
	# End

	def disableResize():
		app.resizable(False, False)

	app = tk.Toplevel()
	app.iconbitmap(resource_path('icon/app.ico'))
	app.title("Advance Brawlhalla Macro by Necode")
	app.after(1000, disableResize)


	def RightLeftRelease():
		if keyboard.is_pressed(RIGHT) == True:
			print("Release key RIGHT")
			keyboard.release(RIGHT)
		if keyboard.is_pressed(LEFT) == True:
			print("Release key LEFT")
			keyboard.release(LEFT)

	def RightLeftReverse():
		if keyboard.is_pressed(RIGHT) == True:
			print("[Reverse]: Press key LEFT")
			keyboard.press(LEFT)
			keyboard.release(LEFT)
		if keyboard.is_pressed(LEFT) == True:
			print("[Reverse]: Press key RIGHT")
			keyboard.press(RIGHT)
			keyboard.release(RIGHT)

	def UpDownReease():
		if keyboard.is_pressed(UP) == True:
			print("Release key UP")
			keyboard.release(UP)
		if keyboard.is_pressed(DOWN) == True:
			print("Release key DOWN")
			keyboard.release(DOWN)

	####################################################################

	def onComboType0(event):
		if event.name == CType0Text.get():
			print('Orb: SLight -> Jump -> SAir')
			# Movement 1
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# Delay 1
			time.sleep(0.5)
			# Movement 2
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)

	def onComboType1(event):
		if event.name == CType1Text.get():
			print('Unarmed: DLight -> Jump -> GP')
			# Movement 1
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			time.sleep(0.22)
			# Movement 2
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			# Delay 2
			time.sleep(0.05)
			# Movement 3
			keyboard.press(DOWN)
			keyboard.press(HeavyAttack)
			keyboard.release(DOWN)
			keyboard.release(HeavyAttack)

	def onComboType2(event):
		if event.name == CType2Text.get():
			print('Unarmed: DLight -> Jump -> NAir')
			# Movement 1
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			time.sleep(0.22)
			# Movement 2
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			# Delay 2
			time.sleep(0.05)
			# Movement 3
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)

	def onComboType3(event):
		if event.name == CType3Text.get():
			print('Sword: DLight -> Jump -> SAir')
			# Movement 1
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			time.sleep(0.45)
			# Movement 2
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)

	def onComboType4(event):
		if event.name == CType4Text.get():
			print('Sword: DLight -> NAir')
			# Movement 1
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			time.sleep(0.45)
			# Movement 2
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)

	def onComboType5(event):
		if event.name == CType5Text.get():
			print('Sword: DLight -> Jump -> DAir')
			# Movement 1
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			time.sleep(0.45)
			# Movement 2
			keyboard.press(JUMP)
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)

	def onComboType6(event):
		if event.name == CType6Text.get():
			print('Sword: DLight -> Jump -> Recovery')
			# Movement 1
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			time.sleep(0.45)
			# Movement 2
			keyboard.press(JUMP)
			keyboard.press(UP)
			keyboard.press(HeavyAttack)
			keyboard.release(JUMP)
			keyboard.release(UP)
			keyboard.release(HeavyAttack)

	def onComboType7(event):
		if event.name == CType7Text.get():
			print('Lance: SLight -> Jump -> SAir/NAir') # Also work with NAir if you don't press left or right
			# Movement 1
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# delay 1
			time.sleep(0.4)
			# Movement 2
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)

	def onComboType8(event):
		if event.name == CType8Text.get():
			print('Lance: SLight -> Jump -> Recovery')
			# Movement 1
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# delay 1
			time.sleep(0.4)
			# Movement 2
			keyboard.press(JUMP)
			keyboard.press(HeavyAttack)
			keyboard.release(JUMP)
			keyboard.release(HeavyAttack)

	def onComboType9(event):
		if event.name == CType9Text.get():
			print('Lance: SLight -> Jump -> DAir')
			# Movement 1
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# delay 1
			time.sleep(0.41)
			# Movement 2
			keyboard.press(JUMP)
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)

	def onComboType10(event):
		if event.name == CType10Text.get():
			print('Hammer: DLight -> Jump -> DAir')
			# Movement 1
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay
			time.sleep(0.3)
			# Movement 2
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)

	def onComboType11(event):
		if event.name == CType11Text.get():
			print('Hammer: DLight -> Jump -> SAir')
			# Movement 1
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay
			time.sleep(0.35)
			# Movement 2
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)

	def onComboType12(event):
		if event.name == CType12Text.get(): # Press left or right required
			print('Hammer: DLight -> Jump -> FDodge -> Recovery')
			# Movement 1
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay 1
			time.sleep(0.4)
			# Movement 2
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			keyboard.press(DODGE)
			keyboard.press(HeavyAttack)
			# Delay 3
			time.sleep(0.12)
			# Movement 4
			keyboard.release(DODGE)
			keyboard.release(HeavyAttack)

	def onComboType13(event):
		if event.name == CType13Text.get(): # Press left or right required
			print('Blaster: DLight -> Jump -> DAir')
			# Movement 1
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay
			time.sleep(0.7)
			# Movement 2
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			
	def onComboType14(event):
		if event.name == CType14Text.get():
			print('Blaster: DLight -> Jump -> Recovery')
			# Movement 1
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay
			time.sleep(0.7)
			# Movement 2
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.release(DOWN)
			keyboard.press(HeavyAttack)

			keyboard.release(DODGE)
			keyboard.release(JUMP)
			keyboard.release(HeavyAttack)
		
	def onComboType15(event):
		if event.name == CType15Text.get():
			# THIS IS THE HARDEST GAUNTLET COMBO, I SPENT 6HOURS JUST TO ADJUST THI DAMN COMBO
			# YOU MAY GET 70%/50% CHANCE DOING RANDOM COMBO WITH THIS
			print('Gauntlet: DLight -> Jump -> CDodge -> NAir')
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay 1
			time.sleep(0.4)
			# Movement 2
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			keyboard.press(DODGE)
			keyboard.press(UP)
			keyboard.press(LightAttack)
			# Delay 3
			time.sleep(0.12)
			# Movement 4
			keyboard.release(DODGE)
			keyboard.release(UP)
			keyboard.release(LightAttack)

	def onComboType16(event):
		if event.name == CType16Text.get():
			print('Greatsword')
			# Movement 1
			keyboard.press(UP)
			keyboard.press(LightAttack)
			print("NLight")
			keyboard.release(UP)
			keyboard.release(LightAttack)
			# Delay 1
			time.sleep(0.3)
			# Movement 2
			UpDownReease()
			keyboard.press(LightAttack)
			print("SLight")
			keyboard.release(LightAttack)
			# Delay 2
			time.sleep(0.4)
			# Movement 3
			print("CD")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.release(DODGE)

	def onComboType17(event):
		if event.name == CType17Text.get(): # Press left or right required
			print('Greatsword')
			# Movement 1
			keyboard.press(LightAttack)
			print("SLight")
			keyboard.release(LightAttack)
			# Delay 1
			time.sleep(0.3)
			# Movement 2
			RightLeftRelease()
			keyboard.press(UP)
			keyboard.press(LightAttack)
			print("NLight")
			keyboard.release(UP)
			keyboard.release(LightAttack)
			# Delay 2
			time.sleep(0.4)
			# Movement 3
			print("CD")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.release(DODGE)

	def onComboType18(event):
		if event.name == CType18Text.get():
			print('Greatsword')
			# Movement 1
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			print("DLight")
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay 1
			time.sleep(0.4)
			# Movement 2
			RightLeftRelease()
			keyboard.press(UP)
			keyboard.press(LightAttack)
			print("NLight")
			keyboard.release(UP)
			keyboard.release(LightAttack)
			# Delay 2
			time.sleep(0.4)
			# Movement 3
			print("CD")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.release(DODGE)

	# def onComboType19(event):
	# 	if event.name == CType19Text.get():
	# 		print("DELETED COMBO")

	# def onComboType20(event):
	# 	if event.name == CType20Text.get():
	# 		print('NOTHING')

	keyboard.on_press(onComboType1)
	keyboard.on_press(onComboType0)
	keyboard.on_press(onComboType2)
	keyboard.on_press(onComboType3)
	keyboard.on_press(onComboType4)
	keyboard.on_press(onComboType5)
	keyboard.on_press(onComboType6)
	keyboard.on_press(onComboType7)
	keyboard.on_press(onComboType8)
	keyboard.on_press(onComboType9)
	keyboard.on_press(onComboType10)
	keyboard.on_press(onComboType11)
	keyboard.on_press(onComboType12)
	keyboard.on_press(onComboType13)
	keyboard.on_press(onComboType14)
	keyboard.on_press(onComboType15)
	keyboard.on_press(onComboType16)
	keyboard.on_press(onComboType17)
	keyboard.on_press(onComboType18)
	# keyboard.on_press(onComboType19)
	# keyboard.on_press(onComboType20)

	################################## Command Enable ##################################
	def CType0Cmd():
		print(str(CType0Text.get()))

	def CType1Cmd():
		print(str(CType1Text.get()))

	def CType2Cmd():
		print(str(CType2Text.get()))

	def CType3Cmd():
		print(str(CType3Text.get()))

	def CType4Cmd():
		print(str(CType4Text.get()))

	def CType5Cmd():
		print(str(CType5Text.get()))

	def CType6Cmd():
		print(str(CType6Text.get()))

	def CType7Cmd():
		print(str(CType7Text.get()))

	def CType8Cmd():
		print(str(CType8Text.get()))

	def CType9Cmd():
		print(str(CType9Text.get()))

	def CType10Cmd():
		print(str(CType10Text.get()))

	def CType11Cmd():
		print(str(CType11Text.get()))

	def CType12Cmd():
		print(str(CType12Text.get()))

	def CType13Cmd():
		print(str(CType13Text.get()))

	def CType14Cmd():
		print(str(CType14Text.get()))

	def CType15Cmd():
		print(str(CType15Text.get()))

	def CType16Cmd():
		print(str(CType16Text.get()))

	def CType17Cmd():
		print(str(CType17Text.get()))

	def CType18Cmd():
		print(str(CType18Text.get()))

	# def CType19Cmd():
	# 	print(str(CType19Text.get()))

	# def CType20Cmd():
	# 	print(str(CType20Text.get()))

	################################## Command Disable ##################################
	def CType0DisableCmd():
		print(str(CType0Text.set("SLight -> Jump -> SAir")))

	def CType1DisableCmd():
		print(str(CType1Text.set("DLight -> Jump -> GP")))

	def CType2DisableCmd():
		print(str(CType2Text.set("DLight -> Jump -> NAir")))

	def CType3DisableCmd():
		print(str(CType3Text.set("DLight -> Jump -> SAir")))

	def CType4DisableCmd():
		print(str(CType4Text.set("DLight -> NAir")))

	def CType5DisableCmd():
		print(str(CType5Text.set("DLight -> Jump -> DAir")))

	def CType6DisableCmd():
		print(str(CType6Text.set("DLight -> Jump -> Recovery")))

	def CType7DisableCmd():
		print(str(CType7Text.set("SLight -> Jump -> SAir")))

	def CType8DisableCmd():
		print(str(CType8Text.set("SLight -> Jump -> Recovery")))

	def CType9DisableCmd():
		print(str(CType9Text.set("SLight -> Jump -> DAir")))

	def CType10DisableCmd():
		print(str(CType10Text.set("DLight -> Jump -> DAir")))

	def CType11DisableCmd():
		print(str(CType11Text.set("DLight -> Jump -> SAir")))

	def CType12DisableCmd():
		print(str(CType12Text.set("DLight -> Jump -> FDodge -> Recovery")))

	def CType13DisableCmd():
		print(str(CType13Text.set("DLight -> Jump -> DAir")))

	def CType14DisableCmd():
		print(str(CType14Text.set("DLight -> Jump -> Recovery")))

	def CType15DisableCmd():
		print(str(CType15Text.set("DLight -> Jump -> CDodge -> NAir")))

	def CType16DisableCmd():
		print(str(CType16Text.set("NLight -> SLight -> CD")))

	def CType17DisableCmd():
		print(str(CType17Text.set("SLight -> NLight -> CD")))

	def CType18DisableCmd():
		print(str(CType18Text.set("DLight -> NLight -> CD")))

	# def CType19DisableCmd():
	# 	print(str(CType19Text.set("NLight -> DLight -> CD")))

	# def CType20DisableCmd():
	# 	print(str(CType20Text.set("NOTHING")))

	################################## Label ##################################
	CType0 = Label(app, text="Orb")
	CType0.grid(row=1,column=1)

	CType1 = Label(app, text="Unarmed")
	CType1.grid(row=2,column=1)

	CType2 = Label(app, text="Unarmed")
	CType2.grid(row=3,column=1)

	CType3 = Label(app, text="Sword")
	CType3.grid(row=4,column=1)

	CType4 = Label(app, text="Sword")
	CType4.grid(row=5,column=1)

	CType5 = Label(app, text="Sword")
	CType5.grid(row=6,column=1)

	CType6 = Label(app, text="Sword")
	CType6.grid(row=7,column=1)

	CType7 = Label(app, text="Lance")
	CType7.grid(row=8,column=1)

	CType8 = Label(app, text="Lance")
	CType8.grid(row=9,column=1)

	CType9 = Label(app, text="Lance")
	CType9.grid(row=10,column=1)

	CType10 = Label(app, text="Hammer")
	CType10.grid(row=11,column=1)

	CType11 = Label(app, text="Hammer")
	CType11.grid(row=12,column=1)

	CType12 = Label(app, text="Hammer")
	CType12.grid(row=13,column=1)

	CType13 = Label(app, text="Blaster")
	CType13.grid(row=14,column=1)

	CType14 = Label(app, text="Blaster")
	CType14.grid(row=15,column=1)

	CType15 = Label(app, text="Gauntlet")
	CType15.grid(row=16,column=1)

	CType16 = Label(app, text="Greatsword")
	CType16.grid(row=17,column=1)

	CType17 = Label(app, text="Greatsword")
	CType17.grid(row=18,column=1)

	CType18 = Label(app, text="Greatsword")
	CType18.grid(row=19,column=1)

	# CType19 = Label(app, text="Greatsword")
	# CType19.grid(row=20,column=1)

	# CType20 = Label(app, text="NOTHING")
	# CType20.grid(row=21,column=1)

	################################## Input Box ##################################
	CType0Text		=	StringVar(None)
	CType0Input		=	EntryWithPlaceholder(app, width=35, placeholder="SLight -> Jump -> SAir", textvariable=CType0Text)
	CType0Input.grid(row=1,column=2)

	CType1Text		=	StringVar(None)
	CType1Input		=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> Jump -> GP", textvariable=CType1Text)
	CType1Input.grid(row=2,column=2)

	CType2Text		=	StringVar(None)
	CType2Input		=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> Jump -> NAir", textvariable=CType2Text)
	CType2Input.grid(row=3,column=2)

	CType3Text		=	StringVar(None)
	CType3Input		=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> Jump -> SAir", textvariable=CType3Text)
	CType3Input.grid(row=4,column=2)

	CType4Text		=	StringVar(None)
	CType4Input		=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> NAir", textvariable=CType4Text)
	CType4Input.grid(row=5,column=2)

	CType5Text		=	StringVar(None)
	CType5Input		=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> Jump -> DAir", textvariable=CType5Text)
	CType5Input.grid(row=6,column=2)

	CType6Text		=	StringVar(None)
	CType6Input		=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> Jump -> Recovery", textvariable=CType6Text)
	CType6Input.grid(row=7,column=2)

	CType7Text		=	StringVar(None)
	CType7Input		=	EntryWithPlaceholder(app, width=35, placeholder="SLight -> Jump -> SAir", textvariable=CType7Text)
	CType7Input.grid(row=8,column=2)

	CType8Text		=	StringVar(None)
	CType8Input		=	EntryWithPlaceholder(app, width=35, placeholder="SLight -> Jump -> Recovery", textvariable=CType8Text)
	CType8Input.grid(row=9,column=2)

	CType9Text		=	StringVar(None)
	CType9Input		=	EntryWithPlaceholder(app, width=35, placeholder="SLight -> Jump -> DAir", textvariable=CType9Text)
	CType9Input.grid(row=10,column=2)

	CType10Text		=	StringVar(None)
	CType10Input	=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> Jump -> DAir", textvariable=CType10Text)
	CType10Input.grid(row=11,column=2)

	CType11Text		=	StringVar(None)
	CType11Input	=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> Jump -> SAir", textvariable=CType11Text)
	CType11Input.grid(row=12,column=2)

	CType12Text		=	StringVar(None)
	CType12Input	=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> Jump -> FDodge -> Recovery", textvariable=CType12Text)
	CType12Input.grid(row=13,column=2)

	CType13Text		=	StringVar(None)
	CType13Input	=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> Jump -> DAir", textvariable=CType13Text)
	CType13Input.grid(row=14,column=2)

	CType14Text		=	StringVar(None)
	CType14Input	=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> Jump -> Recovery", textvariable=CType14Text)
	CType14Input.grid(row=15,column=2)

	CType15Text		=	StringVar(None)
	CType15Input	=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> Jump -> CDodge -> NAir", textvariable=CType15Text)
	CType15Input.grid(row=16,column=2)

	CType16Text		=	StringVar(None)
	CType16Input	=	EntryWithPlaceholder(app, width=35, placeholder="NLight -> SLight -> CD", textvariable=CType16Text)
	CType16Input.grid(row=17,column=2)

	CType17Text		=	StringVar(None)
	CType17Input	=	EntryWithPlaceholder(app, width=35, placeholder="SLight -> NLight -> CD", textvariable=CType17Text)
	CType17Input.grid(row=18,column=2)

	CType18Text		=	StringVar(None)
	CType18Input	=	EntryWithPlaceholder(app, width=35, placeholder="DLight -> NLight -> CD", textvariable=CType18Text)
	CType18Input.grid(row=19,column=2)

	# CType19Text		=	StringVar(None)
	# CType19Input	=	EntryWithPlaceholder(app, width=35, placeholder="NLight -> DLight -> CD", textvariable=CType19Text)
	# CType19Input.grid(row=20,column=2)

	# CType20Text		=	StringVar(None)
	# CType20Input	=	EntryWithPlaceholder(app, width=35, placeholder="NOTHING", textvariable=CType20Text)
	# CType20Input.grid(row=21,column=2)

	################################## Acivate ##################################
	CType0Button = ttk.Button(app, text = "Activate", command = CType0Cmd)
	CType0Button.grid(row=1,column=3)

	CType1Button = ttk.Button(app, text = "Activate", command = CType1Cmd)
	CType1Button.grid(row=2,column=3)

	CType2Button = ttk.Button(app, text = "Activate", command = CType2Cmd)
	CType2Button.grid(row=3,column=3)
	#
	CType3Button = ttk.Button(app, text = "Activate", command = CType3Cmd)
	CType3Button.grid(row=4,column=3)

	CType4Button = ttk.Button(app, text = "Activate", command = CType4Cmd)
	CType4Button.grid(row=5,column=3)

	CType5Button = ttk.Button(app, text = "Activate", command = CType5Cmd)
	CType5Button.grid(row=6,column=3)

	CType6Button = ttk.Button(app, text = "Activate", command = CType6Cmd)
	CType6Button.grid(row=7,column=3)

	CType7Button = ttk.Button(app, text = "Activate", command = CType7Cmd)
	CType7Button.grid(row=8,column=3)

	CType8Button = ttk.Button(app, text = "Activate", command = CType8Cmd)
	CType8Button.grid(row=9,column=3)

	CType9Button = ttk.Button(app, text = "Activate", command = CType9Cmd)
	CType9Button.grid(row=10,column=3)

	CType10Button = ttk.Button(app, text = "Activate", command = CType10Cmd)
	CType10Button.grid(row=11,column=3)

	CType11Button = ttk.Button(app, text = "Activate", command = CType11Cmd)
	CType11Button.grid(row=12,column=3)

	CType12Button = ttk.Button(app, text = "Activate", command = CType12Cmd)
	CType12Button.grid(row=13,column=3)

	CType13Button = ttk.Button(app, text = "Activate", command = CType13Cmd)
	CType13Button.grid(row=14,column=3)

	CType14Button = ttk.Button(app, text = "Activate", command = CType14Cmd)
	CType14Button.grid(row=15,column=3)

	CType15Button = ttk.Button(app, text = "Activate", command = CType15Cmd)
	CType15Button.grid(row=16,column=3)

	CType16Button = ttk.Button(app, text = "Activate", command = CType16Cmd)
	CType16Button.grid(row=17,column=3)

	CType17Button = ttk.Button(app, text = "Activate", command = CType17Cmd)
	CType17Button.grid(row=18,column=3)

	CType18Button = ttk.Button(app, text = "Activate", command = CType18Cmd)
	CType18Button.grid(row=19,column=3)

	# CType19Button = ttk.Button(app, text = "Activate", command = CType19Cmd)
	# CType19Button.grid(row=20,column=3)

	# CType20Button = ttk.Button(app, text = "Activate", command = CType20Cmd)
	# CType20Button.grid(row=21,column=3)

	################################## Deactivate ##################################

	CType0DisableButton = ttk.Button(app, text = "Deactivate", command = CType0DisableCmd)
	CType0DisableButton.grid(row=1,column=4)

	CType1DisableButton = ttk.Button(app, text = "Deactivate", command = CType1DisableCmd)
	CType1DisableButton.grid(row=2,column=4)

	CType2DisableButton = ttk.Button(app, text = "Deactivate", command = CType2DisableCmd)
	CType2DisableButton.grid(row=3,column=4)

	CType3DisableButton = ttk.Button(app, text = "Deactivate", command = CType3DisableCmd)
	CType3DisableButton.grid(row=4,column=4)

	CType4DisableButton = ttk.Button(app, text = "Deactivate", command = CType4DisableCmd)
	CType4DisableButton.grid(row=5,column=4)

	CType5DisableButton = ttk.Button(app, text = "Deactivate", command = CType5DisableCmd)
	CType5DisableButton.grid(row=6,column=4)

	CType6DisableButton = ttk.Button(app, text = "Deactivate", command = CType6DisableCmd)
	CType6DisableButton.grid(row=7,column=4)

	CType7DisableButton = ttk.Button(app, text = "Deactivate", command = CType7DisableCmd)
	CType7DisableButton.grid(row=8,column=4)

	CType8DisableButton = ttk.Button(app, text = "Deactivate", command = CType8DisableCmd)
	CType8DisableButton.grid(row=9,column=4)

	CType9DisableButton = ttk.Button(app, text = "Deactivate", command = CType9DisableCmd)
	CType9DisableButton.grid(row=10,column=4)

	CType10DisableButton = ttk.Button(app, text = "Deactivate", command = CType10DisableCmd)
	CType10DisableButton.grid(row=11,column=4)

	CType11DisableButton = ttk.Button(app, text = "Deactivate", command = CType11DisableCmd)
	CType11DisableButton.grid(row=12,column=4)

	CType12DisableButton = ttk.Button(app, text = "Deactivate", command = CType12DisableCmd)
	CType12DisableButton.grid(row=13,column=4)

	CType13DisableButton = ttk.Button(app, text = "Deactivate", command = CType13DisableCmd)
	CType13DisableButton.grid(row=14,column=4)

	CType14DisableButton = ttk.Button(app, text = "Deactivate", command = CType14DisableCmd)
	CType14DisableButton.grid(row=15,column=4)

	CType15DisableButton = ttk.Button(app, text = "Deactivate", command = CType15DisableCmd)
	CType15DisableButton.grid(row=16,column=4)

	CType16DisableButton = ttk.Button(app, text = "Deactivate", command = CType16DisableCmd)
	CType16DisableButton.grid(row=17,column=4)

	CType17DisableButton = ttk.Button(app, text = "Deactivate", command = CType17DisableCmd)
	CType17DisableButton.grid(row=18,column=4)

	CType18DisableButton = ttk.Button(app, text = "Deactivate", command = CType18DisableCmd)
	CType18DisableButton.grid(row=19,column=4)

	# CType19DisableButton = ttk.Button(app, text = "Deactivate", command = CType19DisableCmd)
	# CType19DisableButton.grid(row=20,column=4)

	# CType20DisableButton = ttk.Button(app, text = "Deactivate", command = CType20DisableCmd)
	# CType20DisableButton.grid(row=21,column=4)

	app.mainloop()