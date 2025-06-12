def	generate_key(n):
	letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	key = {}
	cnt = 0

	for c in letters:
		key[c] = letters[(cnt + n) % len(letters)]
		cnt += 1

	return key

def	encrypt(key, message):
	secret = ""

	for letter in message:
		if letter in key:
			secret += key[letter]
		else:
			secret += letter

	return secret

key = generate_key(3)
message = input("Enter the message to encrypt: ")
secret = encrypt(key, message)
print(secret)
