import tkinter as tk
from tkinter import Button, Frame, Entry, Label, ttk, StringVar, PhotoImage
import os
import sys
from inputs import keyinputs
import keyboard
from time import sleep

# Module Name and Label Name
thisName = "Axe"
# End

# Provide relative path to packed file
def resource_path(relative_path):
	try:
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")
	return os.path.join(base_path, relative_path)
# End

# Disabled Close X button
def disableX():
	pass
# End

def OpenApp():
	class App:
		def __init__(self, root):
			self.frameDB = []
			self.entryDB = []
			self.custmDB = []
			self.functDB = []
			self.count = 0
			self.root = root
			self.appMarg = tk.LabelFrame(self.root, text="Custom", padx=5, pady=5)
			self.appMarg.pack(padx=5, pady=5)
			self.exit = ttk.Button(self.root, text="Exit", command=self.exit, width=20)
			self.exit.pack(side="bottom")
			self.new = ttk.Button(self.root, text="New", command=self.draw, width=20)
			self.new.pack(side="bottom")
		def exit(self):
			def setDefaultValue():
				for i in range(self.count):
					Movement1 = self.entryDB[i][0]
					Delay0 = self.entryDB[i][1]
					Movement2 = self.entryDB[i][2]
					Delay1 = self.entryDB[i][3]
					Movement3 = self.entryDB[i][4]
					KeyInput = self.entryDB[i][5]
					Movement1.set("None")
					Delay0.set("Delay")
					Movement2.set("None")
					Delay1.set("Delay")
					Movement3.set("None")
					KeyInput.set("key")
				clearAllitem()
			# Delete data
			def clearAllitem():
				self.frameDB.clear()
				self.entryDB.clear()
				self.custmDB.clear()
				self.functDB.clear()
				closeChildWin()
			# Wait for 0.2 then close window
			def closeChildWin():
				if not self.count == 0:
					self.count -= self.count
				if self.count == 0:
					self.root.destroy()
			# Set default > Clear Item > Close
			setDefaultValue()
		def draw(self):
			self.frameDB.append(Frame(self.appMarg, borderwidth=1, relief="solid"))
			self.frameDB[self.count].pack(side="top")

			# Label
			self.fWeaponLabel = tk.Label(self.frameDB[self.count], text=thisName)
			self.fWeaponLabel.grid(row=1, column=1)

			# First Combo
			WeaponInpt1Txt = StringVar(None)
			WeaponInpt1 = ttk.Combobox(self.frameDB[self.count], width=15, textvariable=WeaponInpt1Txt, state='readonly')
			WeaponInpt1['values'] = ('None', 'Neutral Heavy', 'Down Heavy', 'Side Heavy', 'Neutral Light', 'Down Light', 'Side Light', 'Recovery', 'GroundPound', 'Neutral Air', 'Down Air', 'Side Air', 'Jump', 'Dash Jump', 'Fast Fall', 'Dodge up', 'Dodge down', 'Forward Dodge', 'Throw', 'Pickup')
			WeaponInpt1.set('None')
			WeaponInpt1.grid(row=1, column=4)

			# Delay Duration
			InputDelay1Txt = StringVar(None)
			InputDelay1 = ttk.Combobox(self.frameDB[self.count], width=5, textvariable=InputDelay1Txt, state='readonly')
			InputDelay1['values'] = ('Delay', 0, 0.1, 0.15, 0.20, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1)
			InputDelay1.set('Delay')
			InputDelay1.grid(row=1, column=5)

			# Second Combo
			WeaponInpt2Txt = StringVar(None)
			WeaponInpt2 = ttk.Combobox(self.frameDB[self.count], width=15, textvariable=WeaponInpt2Txt, state='readonly')
			WeaponInpt2['values'] = ('None', 'Neutral Heavy', 'Down Heavy', 'Side Heavy', 'Neutral Light', 'Down Light', 'Side Light', 'Recovery', 'GroundPound', 'Neutral Air', 'Down Air', 'Side Air', 'Jump', 'Dash Jump', 'Fast Fall', 'Dodge up', 'Dodge down', 'Forward Dodge', 'Throw', 'Pickup')
			WeaponInpt2.set('None')
			WeaponInpt2.grid(row=1, column=6)

			# Delay Duration
			InputDelay2Txt = StringVar(None)
			InputDelay2 = ttk.Combobox(self.frameDB[self.count], width=5, textvariable=InputDelay2Txt, state='readonly')
			InputDelay2['values'] = ('Delay', 0, 0.1, 0.15, 0.20, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1)
			InputDelay2.set('Delay')
			InputDelay2.grid(row=1, column=7)

			# Third Combo
			WeaponInpt3Txt = StringVar(None)
			WeaponInpt3 = ttk.Combobox(self.frameDB[self.count], width=15, textvariable=WeaponInpt3Txt, state='readonly')
			WeaponInpt3['values'] = ('None', 'Neutral Heavy', 'Down Heavy', 'Side Heavy', 'Neutral Light', 'Down Light', 'Side Light', 'Recovery', 'GroundPound', 'Neutral Air', 'Down Air', 'Side Air', 'Jump', 'Dash Jump', 'Fast Fall', 'Dodge up', 'Dodge down', 'Forward Dodge', 'Throw', 'Pickup')
			WeaponInpt3.set('None')
			WeaponInpt3.grid(row=1, column=8)

			# Delay Duration
			InputDelay3Txt = StringVar(None)
			InputDelay3 = ttk.Combobox(self.frameDB[self.count], width=5, textvariable=InputDelay3Txt, state='readonly')
			InputDelay3['values'] = ('Delay', 0, 0.1, 0.15, 0.20, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1)
			InputDelay3.set('Delay')
			InputDelay3.grid(row=1, column=9)

			# Third Combo
			WeaponInpt4Txt = StringVar(None)
			WeaponInpt4 = ttk.Combobox(self.frameDB[self.count], width=15, textvariable=WeaponInpt4Txt, state='readonly')
			WeaponInpt4['values'] = ('None', 'Neutral Heavy', 'Down Heavy', 'Side Heavy', 'Neutral Light', 'Down Light', 'Side Light', 'Recovery', 'GroundPound', 'Neutral Air', 'Down Air', 'Side Air', 'Jump', 'Dash Jump', 'Fast Fall', 'Dodge up', 'Dodge down', 'Forward Dodge', 'Throw', 'Pickup')
			WeaponInpt4.set('None')
			WeaponInpt4.grid(row=1, column=10)

			# Delay Duration
			InputDelay4Txt = StringVar(None)
			InputDelay4 = ttk.Combobox(self.frameDB[self.count], width=5, textvariable=InputDelay4Txt, state='readonly')
			InputDelay4['values'] = ('Delay', 0, 0.1, 0.15, 0.20, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95, 1)
			InputDelay4.set('Delay')
			InputDelay4.grid(row=1, column=11)

			# Third Combo
			WeaponInpt5Txt = StringVar(None)
			WeaponInpt5 = ttk.Combobox(self.frameDB[self.count], width=15, textvariable=WeaponInpt5Txt, state='readonly')
			WeaponInpt5['values'] = ('None', 'Neutral Heavy', 'Down Heavy', 'Side Heavy', 'Neutral Light', 'Down Light', 'Side Light', 'Recovery', 'GroundPound', 'Neutral Air', 'Down Air', 'Side Air', 'Jump', 'Dash Jump', 'Fast Fall', 'Dodge up', 'Dodge down', 'Forward Dodge', 'Throw', 'Pickup')
			WeaponInpt5.set('None')
			WeaponInpt5.grid(row=1, column=12)

			# Key to use
			ChooseKeyTxt = StringVar(None)
			ChooseKey = ttk.Combobox(self.frameDB[self.count], width=5, textvariable=ChooseKeyTxt, state='readonly')
			ChooseKey['values'] = ('key', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
			ChooseKey.set('key')
			ChooseKey.grid(row=1, column=13)

			# Reset
			resetCustom = ttk.Button(self.frameDB[self.count], text="Reset", command=lambda counter=self.count: self.ResetCustom(counter=counter))
			resetCustom.grid(row=1, column=14)

			# Create
			createCustom = ttk.Button(self.frameDB[self.count], text="Create", command=lambda counter=self.count: self.CreateCustom(Mov1=WeaponInpt1Txt.get(), Dly=InputDelay1Txt.get(), Mov2= WeaponInpt2Txt.get(), Dly1=InputDelay2Txt.get(), Mov3=WeaponInpt3Txt.get(), Dly2=InputDelay3Txt.get(), Mov4=WeaponInpt4Txt.get(), Dly3=InputDelay4Txt.get(), Mov5=WeaponInpt5Txt.get(), Key=ChooseKeyTxt.get(), counter=counter)) 
			createCustom.grid(row=1, column=15)

			# Array data
			self.custmDB.append([createCustom])
			self.entryDB.append([WeaponInpt1, InputDelay1, WeaponInpt2, InputDelay2, WeaponInpt3, InputDelay3, WeaponInpt4, InputDelay4, WeaponInpt5, ChooseKey])
			self.count += 1

		# Create Custom
		def CreateCustom(self, Mov1, Dly, Mov2, Dly1, Mov3, Dly2, Mov4, Dly3, Mov5, Key, counter):
			print(f"############ Widget Discrim {counter} added #############")
			def Play(event):
				try:
					Movement1 = self.entryDB[counter][0]
					Delay0 = self.entryDB[counter][1]
					Movement2 = self.entryDB[counter][2]
					Delay1 = self.entryDB[counter][3]
					Movement3 = self.entryDB[counter][4]
					Delay2 = self.entryDB[counter][5]
					Movement4 = self.entryDB[counter][6]
					Delay3 = self.entryDB[counter][7]
					Movement5 = self.entryDB[counter][8]
					KeyInput = self.entryDB[counter][9]
					if event.name == KeyInput.get():
						print(f"It works from discrim {counter}")
						if Movement1.get() == "Neutral Heavy":
							keyinputs.Neutral_Heavy_Attack()
						if Movement1.get() == "Down Heavy":
							keyinputs.Down_Heavy_Attack()
						if Movement1.get() == "Side Heavy":
							keyinputs.Side_Heavy_Attack()
						if Movement1.get() == "Neutral Light":
							keyinputs.Neutral_Light_Attack()
						if Movement1.get() == "Down Light":
							keyinputs.Down_Light_Attack()
						if Movement1.get() == "Side Light":
							keyinputs.Side_Light_Attack()
						if Movement1.get() == "Recovery":
							keyinputs.Recovery()
						if Movement1.get() == "GroundPound":
							keyinputs.GroundPound()
						if Movement1.get() == "Neutral Air":
							keyinputs.Neutral_Air()
						if Movement1.get() == "Down Air":
							keyinputs.Down_Air()
						if Movement1.get() == "Side Air":
							keyinputs.Side_Air()
						if Movement1.get() == "Jump":
							keyinputs.Jump()
						if Movement1.get() == "Dash Jump":
							keyinputs.Dash_Jump()
						if Movement1.get() == "Fast Fall":
							keyinputs.Fast_Fall()
						if Movement1.get() == "Dodge up":
							keyinputs.Up_Dodge()
						if Movement1.get() == "Dodge down":
							keyinputs.Down_Dodge()
						if Movement1.get() == "Forward Dodge":
							keyinputs.Forward_Dodge()
						if Movement1.get() == "Throw":
							keyinputs.Throw()
						if Movement1.get() == "Pickup":
							keyinputs.Pickup()
						sleep(float(Delay0.get()))
						if Movement2.get() == "Neutral Heavy":
							keyinputs.Neutral_Heavy_Attack()
						if Movement2.get() == "Down Heavy":
							keyinputs.Down_Heavy_Attack()
						if Movement2.get() == "Side Heavy":
							keyinputs.Side_Heavy_Attack()
						if Movement2.get() == "Neutral Light":
							keyinputs.Neutral_Light_Attack()
						if Movement2.get() == "Down Light":
							keyinputs.Down_Light_Attack()
						if Movement2.get() == "Side Light":
							keyinputs.Side_Light_Attack()
						if Movement2.get() == "Recovery":
							keyinputs.Recovery()
						if Movement2.get() == "GroundPound":
							keyinputs.GroundPound()
						if Movement2.get() == "Neutral Air":
							keyinputs.Neutral_Air()
						if Movement2.get() == "Down Air":
							keyinputs.Down_Air()
						if Movement2.get() == "Side Air":
							keyinputs.Side_Air()
						if Movement2.get() == "Jump":
							keyinputs.Jump()
						if Movement2.get() == "Dash Jump":
							keyinputs.Dash_Jump()
						if Movement2.get() == "Fast Fall":
							keyinputs.Fast_Fall()
						if Movement2.get() == "Dodge up":
							keyinputs.Up_Dodge()
						if Movement2.get() == "Dodge down":
							keyinputs.Down_Dodge()
						if Movement2.get() == "Forward Dodge":
							keyinputs.Forward_Dodge()
						if Movement2.get() == "Throw":
							keyinputs.Throw()
						if Movement2.get() == "Pickup":
							keyinputs.Pickup()
						sleep(float(Delay1.get()))
						if Movement3.get() == "Neutral Heavy":
							keyinputs.Neutral_Heavy_Attack()
						if Movement3.get() == "Down Heavy":
							keyinputs.Down_Heavy_Attack()
						if Movement3.get() == "Side Heavy":
							keyinputs.Side_Heavy_Attack()
						if Movement3.get() == "Neutral Light":
							keyinputs.Neutral_Light_Attack()
						if Movement3.get() == "Down Light":
							keyinputs.Down_Light_Attack()
						if Movement3.get() == "Side Light":
							keyinputs.Side_Light_Attack()
						if Movement3.get() == "Recovery":
							keyinputs.Recovery()
						if Movement3.get() == "GroundPound":
							keyinputs.GroundPound()
						if Movement3.get() == "Neutral Air":
							keyinputs.Neutral_Air()
						if Movement3.get() == "Down Air":
							keyinputs.Down_Air()
						if Movement3.get() == "Side Air":
							keyinputs.Side_Air()
						if Movement3.get() == "Jump":
							keyinputs.Jump()
						if Movement3.get() == "Dash Jump":
							keyinputs.Dash_Jump()
						if Movement3.get() == "Fast Fall":
							keyinputs.Fast_Fall()
						if Movement3.get() == "Dodge up":
							keyinputs.Up_Dodge()
						if Movement3.get() == "Dodge down":
							keyinputs.Down_Dodge()
						if Movement3.get() == "Forward Dodge":
							keyinputs.Forward_Dodge()
						if Movement3.get() == "Throw":
							keyinputs.Throw()
						if Movement3.get() == "Pickup":
							keyinputs.Pickup()
						sleep(float(Delay2.get()))
						if Movement4.get() == "Neutral Heavy":
							keyinputs.Neutral_Heavy_Attack()
						if Movement4.get() == "Down Heavy":
							keyinputs.Down_Heavy_Attack()
						if Movement4.get() == "Side Heavy":
							keyinputs.Side_Heavy_Attack()
						if Movement4.get() == "Neutral Light":
							keyinputs.Neutral_Light_Attack()
						if Movement4.get() == "Down Light":
							keyinputs.Down_Light_Attack()
						if Movement4.get() == "Side Light":
							keyinputs.Side_Light_Attack()
						if Movement4.get() == "Recovery":
							keyinputs.Recovery()
						if Movement4.get() == "GroundPound":
							keyinputs.GroundPound()
						if Movement4.get() == "Neutral Air":
							keyinputs.Neutral_Air()
						if Movement4.get() == "Down Air":
							keyinputs.Down_Air()
						if Movement4.get() == "Side Air":
							keyinputs.Side_Air()
						if Movement4.get() == "Jump":
							keyinputs.Jump()
						if Movement4.get() == "Dash Jump":
							keyinputs.Dash_Jump()
						if Movement4.get() == "Fast Fall":
							keyinputs.Fast_Fall()
						if Movement4.get() == "Dodge up":
							keyinputs.Up_Dodge()
						if Movement4.get() == "Dodge down":
							keyinputs.Down_Dodge()
						if Movement4.get() == "Forward Dodge":
							keyinputs.Forward_Dodge()
						if Movement4.get() == "Throw":
							keyinputs.Throw()
						if Movement4.get() == "Pickup":
							keyinputs.Pickup()
						sleep(float(Delay3.get()))
						if Movement5.get() == "Neutral Heavy":
							keyinputs.Neutral_Heavy_Attack()
						if Movement5.get() == "Down Heavy":
							keyinputs.Down_Heavy_Attack()
						if Movement5.get() == "Side Heavy":
							keyinputs.Side_Heavy_Attack()
						if Movement5.get() == "Neutral Light":
							keyinputs.Neutral_Light_Attack()
						if Movement5.get() == "Down Light":
							keyinputs.Down_Light_Attack()
						if Movement5.get() == "Side Light":
							keyinputs.Side_Light_Attack()
						if Movement5.get() == "Recovery":
							keyinputs.Recovery()
						if Movement5.get() == "GroundPound":
							keyinputs.GroundPound()
						if Movement5.get() == "Neutral Air":
							keyinputs.Neutral_Air()
						if Movement5.get() == "Down Air":
							keyinputs.Down_Air()
						if Movement5.get() == "Side Air":
							keyinputs.Side_Air()
						if Movement5.get() == "Jump":
							keyinputs.Jump()
						if Movement5.get() == "Dash Jump":
							keyinputs.Dash_Jump()
						if Movement5.get() == "Fast Fall":
							keyinputs.Fast_Fall()
						if Movement5.get() == "Dodge up":
							keyinputs.Up_Dodge()
						if Movement5.get() == "Dodge down":
							keyinputs.Down_Dodge()
						if Movement5.get() == "Forward Dodge":
							keyinputs.Forward_Dodge()
						if Movement5.get() == "Throw":
							keyinputs.Throw()
						if Movement5.get() == "Pickup":
							keyinputs.Pickup()
				except Exception as e:
					# print(f"An error occurred {e}")
					pass
			# Add function to storage
			self.functDB.append([Play])

			# Add event for each stored data
			for i in self.functDB[counter]:
				keyboard.on_press(i)
				print(f"[Info] new event for Discrim {counter}.")

			# Disabled button
			for i in self.custmDB[counter]:
				i['state'] = "disabled"

		# Enable Button
		def ResetCustom(self, counter):
			Movement1 = self.entryDB[counter][0]
			Delay0 = self.entryDB[counter][1]
			Movement2 = self.entryDB[counter][2]
			Delay1 = self.entryDB[counter][3]
			Movement3 = self.entryDB[counter][4]
			Delay2 = self.entryDB[counter][5]
			Movement4 = self.entryDB[counter][6]
			Delay3 = self.entryDB[counter][7]
			Movement5 = self.entryDB[counter][8]
			KeyInput = self.entryDB[counter][9]
			Movement1.set("None")
			Delay0.set("Delay")
			Movement2.set("None")
			Delay1.set("Delay")
			Movement3.set("None")
			Delay2.set("Delay")
			Movement4.set("None")
			Delay3.set("Delay")
			Movement5.set("None")
			KeyInput.set("key")

	# Child window
	childWin = tk.Toplevel()
	childWin.iconbitmap(resource_path('icon/app.ico'))
	App(childWin)

	# Choosen Combo
	appMarg = tk.LabelFrame(childWin, text="Custom", padx=5, pady=5)
	appMarg.pack(padx=5, pady=5)

	# # Disable close [x]
	childWin.protocol("WM_DELETE_WINDOW", disableX)
	def resizable():
		childWin.resizable(False, False)
	childWin.after(100, resizable)
	childWin.state(newstate="normal")
	childWin.mainloop()