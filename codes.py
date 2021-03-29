from base64 import b64encode, b64decode
from datetime import datetime

dateToday = str(datetime.date(datetime.now()))

def stringToBase64(string):
	return b64encode(string.encode('utf-8'))

def base64ToString(base64):
	return b64decode(base64).decode('utf-8')

def reverseString(string):
	return string[::-1]

encodeBase64rest = stringToBase64(string=dateToday)
encodeBase64edit = str(encodeBase64rest).replace("b'", "").replace("'","")

print(reverseString(string="hello"))