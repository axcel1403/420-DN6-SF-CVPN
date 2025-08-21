import math
import random

def	est_premier(p):
	for i in range(2, math.isqrt(p)+1):
		if p % i == 0:
			return False
	return True

def	trouver_premier(size):
	while True:
		p = random.randrange(size, 2*size)
		if est_premier(p):
			return p

def	is_generator(g, p):
	for i in range(1, p - 1):
		if(g**i) % p == 1:
			return False
	return True

def	get_generator(p):
	for g in range(2, p):
		if is_generator(g, p):
			return g

print("46 est non premier : ", est_premier(46))
print("23 est premier : ", est_premier(23))
print("1000 est non premier : ", est_premier(1000))
print("Nombre premier : ", trouver_premier(1000))
p = trouver_premier(10000)
g = get_generator(p)
if is_generator(g, p) == True:
	print("Nombre premier : ", p, "Générateur : ", g)

a = random.randrange(0, p)
j = (g**a) % p
print("Alice j : ", j)
b = random.randrange(0, p)
k = (g**b) % p
print("Bob k : ", k)
g_ab = (k**a) % p
print("Alice g_ab : ", g_ab)
g_ab = (j**b) % p
print("Bob g_ab : ", g_ab)
