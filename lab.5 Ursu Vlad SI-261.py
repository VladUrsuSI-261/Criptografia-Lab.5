mesaj = "Ursu Vlad"

print("Mesaj:", mesaj)

hex_mesaj = mesaj.encode().hex().upper()
dec_mesaj = int.from_bytes(mesaj.encode(), 'big')

print("HEX =", hex_mesaj)
print("DEC =", dec_mesaj)

# =====================
# RSA simplificat
# =====================

p = 61
q = 53

n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = 2753

m = 123

c = pow(m, e, n)
m_decriptat = pow(c, d, n)

print("\n--- RSA ---")
print("Mesaj initial =", m)
print("Mesaj criptat =", c)
print("Mesaj decriptat =", m_decriptat)

# =====================
# Diffie-Hellman
# =====================

p = 23
g = 5

a = 6
b = 15

A = pow(g, a, p)
B = pow(g, b, p)

cheie_alice = pow(B, a, p)
cheie_bob = pow(A, b, p)

print("\n--- Diffie-Hellman ---")
print("Cheia lui Alice =", cheie_alice)
print("Cheia lui Bob =", cheie_bob)

# =====================
# ElGamal simplificat
# =====================

p = 467
g = 2

x = 127
y = pow(g, x, p)

m = 100
k = 53

a = pow(g, k, p)
b = (m * pow(y, k, p)) % p

s = pow(a, x, p)
s_inv = pow(s, -1, p)

m_recuperat = (b * s_inv) % p

print("\n--- ElGamal ---")
print("Mesaj initial =", m)
print("Mesaj criptat =", (a, b))
print("Mesaj decriptat =", m_recuperat)