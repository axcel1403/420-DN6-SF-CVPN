import random

def generate_key():
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	cletters = list(letters)
	key = {}

	for c in letters:
		key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
	return key

def	generate_dkey(key):
	switched_key = {}

	for index, value in key.items():
		switched_key[value] = index

	return switched_key

def	encrypt_decrypt(key, message):
	secret = ""

	for c in message.upper():
		if c in key:
			secret += key[c]
		else:
			secret += c
	return secret

key = generate_key()
message = input("Enter the message to encrypt: ")
secret = encrypt_decrypt(key, message)
print("Encrypted:", secret)

dkey = generate_dkey(key)
message = encrypt_decrypt(dkey, secret)
print("Decrypted:", message)
