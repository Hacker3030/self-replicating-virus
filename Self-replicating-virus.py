import random, string, os, getpass

count = 0
user = getpass.getuser()

while count < 1:
	a = random.choice(string.ascii_uppercase)
	b = random.choice(string.ascii_lowercase)
	c = random.choice(string.ascii_uppercase)
	a_2 = random.choice(string.ascii_lowercase)
	b_2 = random.choice(string.ascii_uppercase)
	c_2 = random.choice(string.ascii_lowercase)

	abc = a + b + c + a_2 + b_2 + c_2

	os.mkdir(f"C:/users/{user}/desktop/{abc}")
