def is_primitive(g, p):
    res = set()
    for i in range(1, p):
        ele = (g**i) % p
        if ele in res:
            return False
        res.add(ele)
    return len(res) == p - 1


def public_key(g, xa, xb, p):
    return (g**xa) % p, (g**xb) % p


def secret_key(xa, xb, ya, yb, p):
    return (yb**xa) % p, (ya**xb) % p


def diffie_hellman():
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter a primitive root (g<p): "))
    while not is_primitive(g, p):
        print("Invalid primitive root.enter again.")
        g = int(input("Enter a primitive root (g<p): "))
    xa = int(input("Enter Private key of A (xa<p): "))
    xb = int(input("Enter Private key of B (xb<p): "))
    ya, yb = public_key(g, xa, xb, p)
    secret_key_A, secret_key_B = secret_key(xa, xb, ya, yb, p)
    if secret_key_A == secret_key_B:
        return ya, yb, secret_key_A


ya, yb, shared_secret = diffie_hellman()
print("A's Public key (ya):", ya)
print("B's Public key (yb):", yb)
print("Shared Secret Key:", shared_secret)
