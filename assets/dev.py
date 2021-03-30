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
	app.title("Advnecode")
	app.after(1000, disableResize)

	appMarg = tk.LabelFrame(app, text="Weapons", padx=5, pady=5)
	appMarg.pack(padx=5, pady=5)


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
			print("Light Attack")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# Delay 1
			print("Wait for 0.5 sec")
			time.sleep(0.5)
			# Movement 2
			print("Jump")
			print("Light Attack")
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			print("==== Orb combo end ====")

	def onComboType1(event):
		if event.name == CType1Text.get():
			print('Unarmed: DLight -> Jump -> GP')
			# Movement 1
			print("Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			print("Wait for 0.22 sec")
			time.sleep(0.22)
			# Movement 2
			print("Jump")
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			# Delay 2
			print("Wait for 0.05 sec")
			time.sleep(0.05)
			# Movement 3
			print("Groundpound")
			keyboard.press(DOWN)
			keyboard.press(HeavyAttack)
			keyboard.release(DOWN)
			keyboard.release(HeavyAttack)
			print("==== Unarmed combo end ====")

	def onComboType2(event):
		if event.name == CType2Text.get():
			print('Unarmed: DLight -> Jump -> NAir')
			# Movement 1
			print("Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			print("Wait for 0.22 sec")
			time.sleep(0.22)
			# Movement 2
			print("Jump")
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			# Delay 2
			print("Wait for 0.55 sec")
			time.sleep(0.05)
			# Movement 3
			print("Neutral Air")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			print("==== Unarmed combo end ====")

	def onComboType3(event):
		if event.name == CType3Text.get():
			print('Sword: DLight -> Jump -> SAir')
			# Movement 1
			print("Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			print("Wait for 0.45 sec")
			time.sleep(0.45)
			# Movement 2
			print("Jump and Light Attack (Side Air when key left or right is pressed)")
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			print("==== Sword combo end ====")

	def onComboType4(event):
		if event.name == CType4Text.get():
			print('Sword: DLight -> NAir')
			# Movement 1
			print("Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			print("Wait for 0.45 sec")
			time.sleep(0.45)
			# Movement 2
			print("Jump and Neutral Attack")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			print("==== Sword combo end ====")

	def onComboType5(event):
		if event.name == CType5Text.get():
			print('Sword: DLight -> Jump -> DAir')
			# Movement 1
			print("Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			print("Wait for 0.45 sec")
			time.sleep(0.45)
			# Movement 2
			print("Jump and Down Air")
			keyboard.press(JUMP)
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			print("==== Sword combo end ====")

	def onComboType6(event):
		if event.name == CType6Text.get():
			print('Sword: DLight -> Jump -> Recovery')
			# Movement 1
			print("Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# delay 1
			print("Wait for 0.455 sec")
			time.sleep(0.45)
			# Movement 2
			print("Jump and Recovery")
			keyboard.press(JUMP)
			keyboard.press(UP)
			keyboard.press(HeavyAttack)
			keyboard.release(JUMP)
			keyboard.release(UP)
			keyboard.release(HeavyAttack)
			print("==== Sword combo end ====")

	def onComboType7(event):
		if event.name == CType7Text.get():
			print('Lance: SLight -> Jump -> SAir/NAir') # Also work with NAir if you don't press left or right
			# Movement 1
			print("Light Attack (Side Light when key left or right is pressed)")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# delay 1
			print("Wait for 0.4 sec")
			time.sleep(0.4)
			# Movement 2
			print("Jump and Side Air when key left or right is pressed and NAir when key left or right is not pressed")
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			print("==== Rocket Lance combo end ====")

	def onComboType8(event):
		if event.name == CType8Text.get():
			print('Lance: SLight -> Jump -> Recovery')
			# Movement 1
			print("Light Attack (Side Light when left or right key is pressed)")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# delay 1
			print("Wait for 0.4 sec")
			time.sleep(0.4)
			# Movement 2
			print("Jump and Recovery (To get chance hitting the opponent, opponent must damaged 80+)")
			keyboard.press(JUMP)
			keyboard.press(HeavyAttack)
			keyboard.release(JUMP)
			keyboard.release(HeavyAttack)
			print("==== Rocke Lance combo end ====")

	def onComboType9(event):
		if event.name == CType9Text.get():
			print('Lance: SLight -> Jump -> DAir')
			# Movement 1
			print("Light Attack (Side Light when left or right key is pressed)")
			keyboard.press(LightAttack)
			keyboard.release(LightAttack)
			# delay 1
			print("Wait for 0.41 (Chance hitting the opponent based on legend dexterity)")
			time.sleep(0.41)
			# Movement 2
			print("Jump and Down Air")
			keyboard.press(JUMP)
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			print("==== Lance combo end ====")

	def onComboType10(event):
		if event.name == CType10Text.get():
			print('Hammer: DLight -> Jump -> DAir')
			# Movement 1
			print("Down Air")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay
			print("Wait for 0.3 (It's really hard to hit the opponent by this combo)")
			time.sleep(0.3)
			# Movement 2
			print("Jump and Down Air")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			print("==== Hammer combo end ====")

	def onComboType11(event):
		if event.name == CType11Text.get():
			print('Hammer: DLight -> Jump -> SAir')
			# Movement 1
			print("Down Light")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay
			print("Wait for 0.35 sec")
			time.sleep(0.35)
			# Movement 2
			print("Jump and Side Air (NAir when key left or right not pressed)")
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			print("==== Hammer combo end ====")

	def onComboType12(event):
		if event.name == CType12Text.get(): # Press left or right required
			print('Hammer: DLight -> Jump -> FDodge -> Recovery')
			# Movement 1
			print("==== Russian bylat Mafia ====")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay 1
			print("Wait for 0.4 sec")
			time.sleep(0.4)
			# Movement 2
			print("Dash Jump and forward dodge a bit following with Hammer Recovery")
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			keyboard.press(DODGE)
			keyboard.press(HeavyAttack)
			# Delay 3
			print("Wait for 0.12 sec")
			time.sleep(0.12)
			# Movement 4
			print("Release dodge and recovery button")
			keyboard.release(DODGE)
			keyboard.release(HeavyAttack)
			print("==== Hammer Russian Mafia end ====")

	def onComboType13(event):
		if event.name == CType13Text.get(): # Press left or right required
			print('Blaster: DLight -> Jump -> DAir')
			# Movement 1
			print("Down Light (Must press key left or right for better chance)")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay
			print("Wait for 0.7 sec")
			time.sleep(0.7)
			# Movement 2
			print("Dash Jmp and Down Air")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			keyboard.release(LightAttack)
			print("==== Blaster combo end ====")

	def onComboType14(event):
		if event.name == CType14Text.get():
			print('Blaster: DLight -> Jump -> Recovery')
			# Movement 1
			print("Down Light (Must press key left or right for better chance)")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay
			print("Wait for 0.7 sec")
			time.sleep(0.7)
			# Movement 2
			print("Jump and Recovery following with Blaster Recovery")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.press(JUMP)
			keyboard.release(DOWN)
			keyboard.press(HeavyAttack)
			print("Release all key for this combo")
			keyboard.release(DODGE)
			keyboard.release(JUMP)
			keyboard.release(HeavyAttack)
			print("==== Blaster combo end ====")

	def onComboType15(event):
		if event.name == CType15Text.get():
			# THIS IS THE HARDEST GAUNTLET COMBO, I SPENT 6HOURS JUST TO ADJUST THI DAMN COMBO
			# YOU MAY GET 70%/50% CHANCE DOING RANDOM COMBO WITH THIS
			print('Gauntlet: DLight -> Jump -> CDodge -> NAir')
			print("Down Light (Also work with GC+DLight in air)")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay 1
			print("Wait for 0.4")
			time.sleep(0.4)
			# Movement 2
			print("Jump and forward dodge a bit following with Neutral Air")
			keyboard.press(JUMP)
			keyboard.release(JUMP)
			keyboard.press(DODGE)
			keyboard.press(UP)
			keyboard.press(LightAttack)
			# Delay 3
			print("Wait for 0.12 sec")
			time.sleep(0.12)
			# Movement 4
			keyboard.release(DODGE)
			keyboard.release(UP)
			keyboard.release(LightAttack)
			print("==== There you go, favorite Gauntlet combo end ====")

	def onComboType16(event):
		if event.name == CType16Text.get():
			print('Greatsword')
			# Movement 1
			print("Release user key up for Neutral Light")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			print("NLight")
			keyboard.release(UP)
			keyboard.release(LightAttack)
			# Delay 1
			print("Wait for 0.3")
			time.sleep(0.3)
			# Movement 2
			UpDownReease()
			keyboard.press(LightAttack)
			print("SLight")
			keyboard.release(LightAttack)
			# Delay 2
			print("Wait for 0.4")
			time.sleep(0.4)
			# Movement 3
			print("CD")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			print("==== Greatsword combo (basic 1) end ====")


	def onComboType17(event):
		if event.name == CType17Text.get():
			print('Greatsword')
			# Movement 1
			print("Side Light (Neutral Attack when user not pressing key left or right)")
			keyboard.press(LightAttack)
			print("SLight")
			keyboard.release(LightAttack)
			# Delay 1
			print("Wait for 0.3 sec")
			time.sleep(0.3)
			# Movement 2
			print("Release key left or right for user")
			RightLeftRelease()
			print("Neutral Light")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			print("NLight")
			keyboard.release(UP)
			keyboard.release(LightAttack)
			# Delay 2
			print("Wait for 0.4 sec")
			time.sleep(0.4)
			# Movement 3
			print("CD")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			print("==== Greatsword combo (basic 2) end ====")

	def onComboType18(event):
		if event.name == CType18Text.get():
			print('Greatsword')
			# Movement 1
			print("Down Light (Best starter for Greatsword combo)")
			keyboard.press(DOWN)
			keyboard.press(LightAttack)
			print("DLight")
			keyboard.release(DOWN)
			keyboard.release(LightAttack)
			# Delay 1
			print("Wait for 0.4 sec")
			time.sleep(0.4)
			# Movement 2
			print("Release key left or right for user")
			RightLeftRelease()
			print("Neutral Light")
			keyboard.press(UP)
			keyboard.press(LightAttack)
			print("NLight")
			keyboard.release(UP)
			keyboard.release(LightAttack)
			# Delay 2
			print("Wait for 0.4 sec")
			time.sleep(0.4)
			# Movement 3
			print("CD")
			keyboard.press(DOWN)
			keyboard.press(DODGE)
			keyboard.release(DOWN)
			keyboard.release(DODGE)
			print("==== Greatsword combo (basic 3) end ====")

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

	################################## Command Disable ##################################
	def CType0DisableCmd():
		CType0Text.set('None')

	def CType1DisableCmd():
		CType1Text.set('None')

	def CType2DisableCmd():
		CType2Text.set('None')

	def CType3DisableCmd():
		CType3Text.set('None')

	def CType4DisableCmd():
		CType4Text.set('None')

	def CType5DisableCmd():
		CType5Text.set('None')

	def CType6DisableCmd():
		CType6Text.set('None')

	def CType7DisableCmd():
		CType7Text.set('None')

	def CType8DisableCmd():
		CType8Text.set('None')

	def CType9DisableCmd():
		CType9Text.set('None')

	def CType10DisableCmd():
		CType10Text.set('None')

	def CType11DisableCmd():
		CType11Text.set('None')

	def CType12DisableCmd():
		CType12Text.set('None')

	def CType13DisableCmd():
		CType13Text.set('None')

	def CType14DisableCmd():
		CType14Text.set('None')

	def CType15DisableCmd():
		CType15Text.set('None')

	def CType16DisableCmd():
		CType16Text.set('None')

	def CType17DisableCmd():
		CType17Text.set('None')

	def CType18DisableCmd():
		CType18Text.set('None')

	################################## Label ##################################
	CType0 = Label(appMarg, text="Orb")
	CType0.grid(row=1,column=1)

	CType1 = Label(appMarg, text="Unarmed")
	CType1.grid(row=2,column=1)

	CType2 = Label(appMarg, text="Unarmed")
	CType2.grid(row=3,column=1)

	CType3 = Label(appMarg, text="Sword")
	CType3.grid(row=4,column=1)

	CType4 = Label(appMarg, text="Sword")
	CType4.grid(row=5,column=1)

	CType5 = Label(appMarg, text="Sword")
	CType5.grid(row=6,column=1)

	CType6 = Label(appMarg, text="Sword")
	CType6.grid(row=7,column=1)

	CType7 = Label(appMarg, text="Lance")
	CType7.grid(row=8,column=1)

	CType8 = Label(appMarg, text="Lance")
	CType8.grid(row=9,column=1)

	CType9 = Label(appMarg, text="Lance")
	CType9.grid(row=10,column=1)

	CType10 = Label(appMarg, text="Hammer")
	CType10.grid(row=11,column=1)

	CType11 = Label(appMarg, text="Hammer")
	CType11.grid(row=12,column=1)

	CType12 = Label(appMarg, text="Hammer")
	CType12.grid(row=13,column=1)

	CType13 = Label(appMarg, text="Blaster")
	CType13.grid(row=14,column=1)

	CType14 = Label(appMarg, text="Blaster")
	CType14.grid(row=15,column=1)

	CType15 = Label(appMarg, text="Gauntlet")
	CType15.grid(row=16,column=1)

	CType16 = Label(appMarg, text="Greatsword")
	CType16.grid(row=17,column=1)

	CType17 = Label(appMarg, text="Greatsword")
	CType17.grid(row=18,column=1)

	CType18 = Label(appMarg, text="Greatsword")
	CType18.grid(row=19,column=1)


	################################## Key ##################################
	CType0Text		=	StringVar(None)
	CType0Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType0Text, state='readonly')
	CType0Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType0Input.set('None')
	CType0Input.grid(row=1,column=2)

	CType1Text		=	StringVar(None)
	CType1Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType1Text, state='readonly')
	CType1Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType1Input.set('None')
	CType1Input.grid(row=2,column=2)

	CType2Text		=	StringVar(None)
	CType2Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType2Text, state='readonly')
	CType2Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType2Input.set('None')
	CType2Input.grid(row=3,column=2)

	CType3Text		=	StringVar(None)
	CType3Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType3Text, state='readonly')
	CType3Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType3Input.set('None')
	CType3Input.grid(row=4,column=2)

	CType4Text		=	StringVar(None)
	CType4Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType4Text, state='readonly')
	CType4Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType4Input.set('None')
	CType4Input.grid(row=5,column=2)

	CType5Text		=	StringVar(None)
	CType5Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType5Text, state='readonly')
	CType5Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType5Input.set('None')
	CType5Input.grid(row=6,column=2)

	CType6Text		=	StringVar(None)
	CType6Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType6Text, state='readonly')
	CType6Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType6Input.set('None')
	CType6Input.grid(row=7,column=2)

	CType7Text		=	StringVar(None)
	CType7Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType7Text, state='readonly')
	CType7Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType7Input.set('None')
	CType7Input.grid(row=8,column=2)

	CType8Text		=	StringVar(None)
	CType8Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType8Text, state='readonly')
	CType8Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType8Input.set('None')
	CType8Input.grid(row=9,column=2)

	CType9Text		=	StringVar(None)
	CType9Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType9Text, state='readonly')
	CType9Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType9Input.set('None')
	CType9Input.grid(row=10,column=2)

	CType10Text		=	StringVar(None)
	CType10Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType10Text, state='readonly')
	CType10Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType10Input.set('None')
	CType10Input.grid(row=11,column=2)

	CType11Text		=	StringVar(None)
	CType11Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType11Text, state='readonly')
	CType11Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType11Input.set('None')
	CType11Input.grid(row=12,column=2)

	CType12Text		=	StringVar(None)
	CType12Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType12Text, state='readonly')
	CType12Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType12Input.set('None')
	CType12Input.grid(row=13,column=2)

	CType13Text		=	StringVar(None)
	CType13Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType13Text, state='readonly')
	CType13Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType13Input.set('None')
	CType13Input.grid(row=14,column=2)

	CType14Text		=	StringVar(None)
	CType14Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType14Text, state='readonly')
	CType14Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType14Input.set('None')
	CType14Input.grid(row=15,column=2)

	CType15Text		=	StringVar(None)
	CType15Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType15Text, state='readonly')
	CType15Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType15Input.set('None')
	CType15Input.grid(row=16,column=2)

	CType16Text		=	StringVar(None)
	CType16Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType16Text, state='readonly')
	CType16Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType16Input.set('None')
	CType16Input.grid(row=17,column=2)

	CType17Text		=	StringVar(None)
	CType17Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType17Text, state='readonly')
	CType17Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType17Input.set('None')
	CType17Input.grid(row=18,column=2)

	CType18Text		=	StringVar(None)
	CType18Input 	=	ttk.Combobox(appMarg, width=5, textvariable=CType18Text, state='readonly')
	CType18Input['values']= ('None', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
	CType18Input.set('None')
	CType18Input.grid(row=19,column=2)

	################################## Reset ##################################

	CType0DisableButton = ttk.Button(appMarg, text = "Reset", command = CType0DisableCmd)
	CType0DisableButton.grid(row=1,column=4)

	CType1DisableButton = ttk.Button(appMarg, text = "Reset", command = CType1DisableCmd)
	CType1DisableButton.grid(row=2,column=4)

	CType2DisableButton = ttk.Button(appMarg, text = "Reset", command = CType2DisableCmd)
	CType2DisableButton.grid(row=3,column=4)

	CType3DisableButton = ttk.Button(appMarg, text = "Reset", command = CType3DisableCmd)
	CType3DisableButton.grid(row=4,column=4)

	CType4DisableButton = ttk.Button(appMarg, text = "Reset", command = CType4DisableCmd)
	CType4DisableButton.grid(row=5,column=4)

	CType5DisableButton = ttk.Button(appMarg, text = "Reset", command = CType5DisableCmd)
	CType5DisableButton.grid(row=6,column=4)

	CType6DisableButton = ttk.Button(appMarg, text = "Reset", command = CType6DisableCmd)
	CType6DisableButton.grid(row=7,column=4)

	CType7DisableButton = ttk.Button(appMarg, text = "Reset", command = CType7DisableCmd)
	CType7DisableButton.grid(row=8,column=4)

	CType8DisableButton = ttk.Button(appMarg, text = "Reset", command = CType8DisableCmd)
	CType8DisableButton.grid(row=9,column=4)

	CType9DisableButton = ttk.Button(appMarg, text = "Reset", command = CType9DisableCmd)
	CType9DisableButton.grid(row=10,column=4)

	CType10DisableButton = ttk.Button(appMarg, text = "Reset", command = CType10DisableCmd)
	CType10DisableButton.grid(row=11,column=4)

	CType11DisableButton = ttk.Button(appMarg, text = "Reset", command = CType11DisableCmd)
	CType11DisableButton.grid(row=12,column=4)

	CType12DisableButton = ttk.Button(appMarg, text = "Reset", command = CType12DisableCmd)
	CType12DisableButton.grid(row=13,column=4)

	CType13DisableButton = ttk.Button(appMarg, text = "Reset", command = CType13DisableCmd)
	CType13DisableButton.grid(row=14,column=4)

	CType14DisableButton = ttk.Button(appMarg, text = "Reset", command = CType14DisableCmd)
	CType14DisableButton.grid(row=15,column=4)

	CType15DisableButton = ttk.Button(appMarg, text = "Reset", command = CType15DisableCmd)
	CType15DisableButton.grid(row=16,column=4)

	CType16DisableButton = ttk.Button(appMarg, text = "Reset", command = CType16DisableCmd)
	CType16DisableButton.grid(row=17,column=4)

	CType17DisableButton = ttk.Button(appMarg, text = "Reset", command = CType17DisableCmd)
	CType17DisableButton.grid(row=18,column=4)

	CType18DisableButton = ttk.Button(appMarg, text = "Reset", command = CType18DisableCmd)
	CType18DisableButton.grid(row=19,column=4)


	def OnExit():
		CType0DisableCmd()
		CType1DisableCmd()
		CType2DisableCmd()
		CType3DisableCmd()
		CType4DisableCmd()
		CType5DisableCmd()
		CType6DisableCmd()
		CType7DisableCmd()
		CType8DisableCmd()
		CType9DisableCmd()
		CType10DisableCmd()
		CType11DisableCmd()
		CType12DisableCmd()
		CType13DisableCmd()
		CType14DisableCmd()
		CType15DisableCmd()
		CType16DisableCmd()
		CType17DisableCmd()
		CType18DisableCmd()
		print('Exit')
		app.destroy()

	ExitAppButton = ttk.Button(app, text="Exit", command=OnExit)
	ExitAppButton.pack(side="bottom")

	def disableX():
		pass
	app.protocol("WM_DELETE_WINDOW", disableX)
	app.mainloop()