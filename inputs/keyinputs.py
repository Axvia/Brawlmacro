import keyboard
import os
import json
from time import sleep

try:
	if os.path.exists(os.getcwd() + '/keybinds.json'):
		# if json file exist, read it!
		with open("./keybinds.json") as f:
			keybindData = json.load(f)
	UP = keybindData["Key Up"]
	DOWN = keybindData["Key Down"]
	RIGHT = keybindData["Key Right"]
	LEFT = keybindData["Key Left"]
	JUMP = keybindData["Key Jump"]
	DODGE = keybindData["Key Dodge"]
	LightAttack = keybindData["Key Light Attack"]
	HeavyAttack = keybindData["Key Heavy Attack"]
	THROW = keybindData["Key Throw"]
	PICKUP = keybindData["Key Pickup"]
except Exception:
	print("keybinds.json not found. Generate new one!")

# Heavy Attack
def Neutral_Heavy_Attack():
	print("Neutral Heavy")
	if keyboard.is_pressed(RIGHT) == True:
		keyboard.release(RIGHT)
		keyboard.press(HeavyAttack)
		keyboard.release(HeavyAttack)
	if keyboard.is_pressed(LEFT) == True:
		keyboard.release(LEFT)
		keyboard.press(HeavyAttack)
		keyboard.release(HeavyAttack)
	# Auto if user not pressing left or right
	keyboard.press(HeavyAttack)
	keyboard.release(HeavyAttack)

def Down_Heavy_Attack():
	print("Down Heavy")
	if keyboard.is_pressed(DOWN) == True:
		keyboard.press(HeavyAttack)
		keyboard.release(HeavyAttack)
	# Auto if user not pressing down
	keyboard.press(DOWN)
	keyboard.press(HeavyAttack)
	keyboard.release(DOWN)
	keyboard.release(HeavyAttack)

def Side_Heavy_Attack():
	print("Side Heavy")
	if keyboard.is_pressed(RIGHT) == True or keyboard.is_pressed(LEFT) == True:
		keyboard.press(HeavyAttack)
		keyboard.release(HeavyAttack)

# Light Attacks
def Neutral_Light_Attack():
	print("Neutral Light")
	if keyboard.is_pressed(RIGHT) == True:
		keyboard.release(RIGHT)
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)
	if keyboard.is_pressed(LEFT) == True:
		keyboard.release(LEFT)
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)
	# Auto if user not pressing left or right
	keyboard.press(LightAttack)
	keyboard.release(LightAttack)

def Down_Light_Attack():
	print("Down Light")
	if keyboard.is_pressed(DOWN) == True:
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)
	# Auto if user not pressing down
	keyboard.press(DOWN)
	keyboard.press(LightAttack)
	keyboard.release(DOWN)
	keyboard.release(LightAttack)

def Side_Light_Attack():
	print("Side Light")
	if keyboard.is_pressed(RIGHT) == True or keyboard.is_pressed(LEFT) == True:
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)

# Aerial Attacks
def Recovery():
	print("Recovery")
	keyboard.press(HeavyAttack)
	keyboard.release(HeavyAttack)

def GroundPound():
	print("GroundPound")
	if keyboard.is_pressed(DOWN) == True:
		keyboard.press(HeavyAttack)
		keyboard.release(HeavyAttack)
	# Auto if user not pressing down
	keyboard.press(DOWN)
	keyboard.press(HeavyAttack)
	keyboard.release(DOWN)
	keyboard.release(HeavyAttack)

def Neutral_Air():
	print("Neutral Air")
	if keyboard.is_pressed(RIGHT) == True:
		keyboard.release(RIGHT)
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)
	if keyboard.is_pressed(LEFT) == True:
		keyboard.release(LEFT)
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)
	# Auto if user not pressing left or right
	keyboard.press(LightAttack)
	keyboard.release(LightAttack)

def Down_Air():
	print("Down Air")
	if keyboard.is_pressed(DOWN) == True:
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)
	# Auto if user not pressing down
	keyboard.press(DOWN)
	keyboard.press(LightAttack)
	keyboard.release(DOWN)
	keyboard.release(LightAttack)

def Side_Air():
	print("Side Air")
	if keyboard.is_pressed(RIGHT) == True or keyboard.is_pressed(LEFT) == True:
		keyboard.press(LightAttack)
		keyboard.release(LightAttack)

# Other
def Jump():
	print("Jump")
	keyboard.press(JUMP)
	keyboard.release(JUMP)

def Dash_Jump():
	print("Dash Jump")
	keyboard.press(DOWN)
	keyboard.press(DODGE)
	keyboard.press(JUMP)
	keyboard.release(DOWN)
	keyboard.release(DODGE)
	keyboard.release(JUMP)

def Fast_Fall():
	print("Fast Fall")
	keyboard.press(DOWN)
	keyboard.release(DOWN)

def Up_Dodge():
	print("Dodge up")
	keyboard.press(DODGE)
	keyboard.press(UP)
	keyboard.release(DODGE)
	keyboard.release(UP)

def Forward_Dodge():
	print("Forward Dodge")
	if keyboard.is_pressed(RIGHT) == True:
		keyboard.press(DODGE)
		sleep(0.3)
		keyboard.release(DODGE)
	if keyboard.is_pressed(LEFT) == True:
		keyboard.press(DODGE)
		sleep(0.3)
		keyboard.release(DODGE)

def Down_Dodge():
	print("Dodge Down")
	if keyboard.is_pressed(DOWN) == True:
		keyboard.press(DODGE)
		keyboard.release(DODGE)
	# Auto if user not pressing down
	keyboard.press(DOWN)
	keyboard.press(DODGE)
	keyboard.release(DOWN)
	keyboard.release(DODGE)

def Throw():
	print("Throw")
	keyboard.press(THROW)
	keyboard.release(THROW)

def Pickup():
	print("Pickup")
	keyboard.press(PICKUP)
	keyboard.release(PICKUP)