import math
import random

def	est_premier(p):
	for i in range(2, math.isqrt(p) + 1):
		if p % i == 0:
			return False
	return True

def	trouver_premier(size):
	while True:
		p = random.randrange(size, 2*size)
		if est_premier(p):
			return p

def	lcm(a, b):
	return a*b//math.gcd(a, b)

def	trouve_e(lambda_n):
	for e in range(2, lambda_n):
		if math.gcd(e, lambda_n) == 1:
			return e
	return False

def	trouve_d(e, lambda_n):
	for d in range(2, lambda_n):
		if d*e % lambda_n == 1:
			return d
	return False

def	facteurs(n):
	for p in range(2, n):
		if n % p == 0:
			return p, n//p

p = trouver_premier(300)
q = trouver_premier(300)
print("Nombres premiers p, q", p, q)
n = p*q
print("Le modulo n : ", n)
lambda_n = lcm(p - 1, q - 1)
print("Lambda_n :", lambda_n)
e = trouve_e(lambda_n)
print("Clé publique (exposant) e :", e)
d = trouve_d(e, lambda_n)
print("Clé secret (exposant) d :", d)

m = 117
c = m**e % n
print("Le message chiffré de Bob :", c)
m = c**d % n
print("Le message pour Alice :", m)
print()

print("Eve peut voir :")
print("La clé publique (e, n) :", e, n)
print("Le message chiffré de Bob :", c)
p, q = facteurs(n)
print("Facteurs d'Eve (p, q) :", p, q)
lambda_n = lcm(p - 1, q - 1)
print("Lambda_n de Eve :", lambda_n)
d = trouve_d(e, lambda_n)
print("Clé secrète (exposant) d'Eve d :", d)
m = c**d % (p*q)
print("Le message pour Eve :", m)

print("+++++++++++++++++")
print("Bob l'imprudent!")
message = "Alice est plus forte que Bob."
for m_c in message:
	c = ord(m_c)**e % n
	print(c, " ", end='')
print("\n+++++++++++++++++")
