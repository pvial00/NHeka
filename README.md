# N Heka

Numerical Heka or N Heka is a practice of divination and magic based around Moon Arithmetic (Modular Arithmetic)

---

# Fetu Cards

Fetu Cards may be used in similar ways to Tarot to give mystical, mathematical and linguistic messages to the reader.  Fetu cards has a simple and unique scoring for the cards in a standard deck.  The Fetu mathematical system enumerates over the symbols on a standard card and assigns value to the value and suit symbols.  (A standard Bicycle Deck or compatible is required to accurately work Fetu Cards).

Fetu Cards in standard operation can generate 52 bits of entropy per deck.  Using the Fetu Max Squeeze Entropy algorithm, one can extract 584 bits of entropy.

---

# NHeka Cipher

This cipher is designed to securely obfuscate hieroglyphic alphabets. Sub Keys are various static lookup tables of numeric arrangements spanning the sequence of the target NHeka modulus.

Expanding upon the Wiqa construction, NHeka comes with optional levels of sub keys.  Sub key lookup tables allow for further raising of the security level by making static substitions of a cipher text with a target sub key.  The order in which the sub keys are applied for encryption are reversed for decryption.

The general operation engine of the cipher is that of Wiqa Cipher A and is a modular arithmetic oriented cipher construction that hasn't been broken.  In addition, with 4 steps per enciphered character, it's fairly fast.  NHeka produces a pseudo-random stream of numbers with highly uniform characteristics.


- Order of Operations

NHeka first applies each sub key transposing the text into a first phase of the cipher text.  Although the general security level of a hieroglyphic system based on only the sub keys is moderately secure, it ultimately may be defeated via frquency.

The next and final stage of NHeka is the application of the Wiqa Cipher sequence and adding the first phase cipher text to the Wiqa sequence.

An optional stage, further complicating matters, would be to substitue the Wiqa cipher text back through an order of the sub keys.
