''' KryptoMagick NHeka Cipher '''
''' '''
''' This cipher is designed to securely obfuscate hieroglyphic alphabets '''
''' Sub Keys are various static lookup tables of numeric arrangements spanning the sequence of the target NHeka modulus '''


class NHekaCipher:
    def __init__(self, modulus=26):
        self.modulus = modulus
        self.alphabet_numbers = list(range(modulus))
        self.alphabet_letters = []
        if modulus <= 26:
            for x in range(modulus):
                alphabet_letters.append(chr(x + 65))

    def keysetup(self, key):
        k = [0] * self.modulus
        j = 0
        for c, byte in enumerate(key):
            k[c] = (k[c] + byte) % self.modulus
            j = (j + (byte) % self.modulus
        return k, j

    def encrypt(self, text, key, sub_keys):
        ctxt = []
        c = 0
        k, j = self.keysetup(key)
        for sub_key in sub_keys:
            ctxt[c] = sub_key.index(ctxt[c])
            c += 1
        c = 0
        for char in text:
            j = k[j]
            k[j] = (k[j] - k[c]) % self.modulus
            output = (k[j] + k[k[j]]) % self.modulus
            sub = (char + output) % self.modulus
            ctxt.append(sub)
            c = (c + 1) % self.modulus
        return ctxt

    def decrypt(self, ctxt, key, sub_keys):
        ptxt = []
        c = 0
        k, j = self.keysetup(key)
        for char in text:
            j = k[j]
            k[j] = (k[j] - k[c]) % self.modulus
            output = (k[j] + k[k[j]]) % self.modulus
            sub = (char - output) % self.modulus
            ptxt.append(sub)
            c = (c + 1) % self.modulus
        c = 0
        for sub_key in reversed(sub_keys):
            ptxt[c] = sub_key[txt[c]]
            c += 1
        return ctxt
