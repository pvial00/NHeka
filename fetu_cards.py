import os
import sys

''' KrypoMagick N Heka Fetu Cards version 'AAB' '''


spade_value = 20
diamond_value = 4
club_value = 10
heart_value = 8

heka_deck_order = {0:'QS', 1:'KS', 2:'JS', 3:'10S', 4:'9S', 5:'8S', 6:'7S', 7:'6S', 8:'5S', 9:'4S', 10:'3S', 11:'2S', 12:'AS', 13:'QD', 14:'KD', 15:'JD', 16:'10D', 17:'9D', 18:'8D', 19:'7D', 20:'6D', 21:'5D', 22:'4D', 23:'3D', 24:'2D', 25:'AD', 26:'QC', 27:'KC', 28:'JC', 29:'10C', 30:'9C', 31:'8C', 32:'7C', 33:'6C', 34:'5C', 35:'4C', 36:'3C', 37:'2C', 38:'AC', 39:'QH', 40:'KH', 41:'JH', 42:'10H', 43:'9H', 44:'8H', 45:'7H', 46:'6H', 47:'5H', 48:'4H', 49:'3H', 50:'2H', 51:'AH'}

heka_deck_order_rev = {'QS':0, 'KS':1, 'JS':2, '10S':3, '9S':4, '8S':5, '7S':6, '6S':7, '5S':8, '4S':9, '3S':10, '2S':11, 'AS':12, 'QD':13, 'KD':14, 'JD':15, '10D':16, '9D':17, '8D':18, '7D':19, '6D':20, '5D':21, '4D':22, '3D':23, '2D':24, 'AD':25, 'QC':26, 'KC':27, 'JC':28, '10C':29, '9C':30, '8C':31, '7C':32, '6C':33, '5C':34, '4C':35, '3C':36, '2C':37, 'AC':38, 'QH':39, 'KH':40, 'JH':41, '10H':42, '9H':43, '8H':44, '7H':45, '6H':46, '5H':47, '4H':48, '3H':49, '2H':50, 'AH':51}

heka_deck_values = [(0, 'QS'), (1, 'KS'), (2, 'JS'), (3, '10S'), (4, '9S'), (5, '8S'), (6, '7S'), (7, '6S'), (8, '5S'), (9, '4S'), (10, '3S'), (11, '2S'), (12, 'AS'), (13, 'QD'), (14, 'KD'), (15, 'JD'), (16, '10D'), (17, '9D'), (18, '8D'), (19, '7D'), (20, '6D'), (21, '5D'), (22, '4D'), (23, '3D'), (24, '2D'), (25, 'AD'), (0, 'QC'), (1, 'KC'), (2, 'JC'), (3, '10C'), (4, '9C'), (5, '8C'), (6, '7C'), (7, '6C'), (8, '5C'), (9, '4C'), (10, '3C'), (11, '2C'), (12, 'AC'), (13, 'QH'), (14, 'KH'), (15, 'JH'), (16, '10H'), (17, '9H'), (18, '8H'), (19, '7H'), (20, '6H'), (21, '5H'), (22, '4H'), (23, '3H'), (24, '2H'), (25, 'AH')]

#heka_deck_fetu_values = [(81, 101, 'QS'), (81, 101, 'KS'), (81, 101, 'JS'), (3, '10S'), (81, 99, '9S'), (81, '8S'), (6, '7S'), (7, '6S'), (8, '5S'), (9, '4S'), (10, '3S'), (11, '2S'), (12, 'AS'), (13, 'QD'), (14, 'KD'), (15, 'JD'), (16, '10D'), (17, '9D'), (18, '8D'), (19, '7D'), (20, '6D'), (21, '5D'), (22, '4D'), (23, '3D'), (24, '2D'), (25, 'AD'), (0:'QC'), (1:'KC', (2:'JC'), (3, '10C'), (4, '9C'), (5, '8C'), (6, '7C'), (7, '6C'), (8, '5C'), (9, '4C'), (10, '3C'), (11, '2C'), (12, 'AC'), (13, 'QH'), (14, 'KH'), (15, 'JH'), (16, '10H'), (17, '9H'), (18, '8H'), (19, '7H'), (20, '6H'), (21, '5H'), (22, '4H'), (23, '3H'), (24, '2H'), (25, 'AH')}

class Card(object):
    order = 0
    fetu = 0
    nhk = 0
    ma = 0
    name = "Card"
    suit_value = 0

def get_card_properties(card_name):
    if len(card_name) == 2:
        num = int(card_name[:1])
        suit = card_name[1:2]
    elif len(card_name) == 3:
        num = int(card_name[:2])
        suit = card_name[2:3]
    if suit == "S":
        suit_value = spade_value
    elif suit == "D":
        suit_value = diamond_value
    elif suit == "C":
        suit_value = club_value
    elif suit == "H":
        suit_value = heart_value
    return num, suit_value

def generate_deck(deck_order):
    deck = []
    for x in range(len(deck_order)):
        card_order_number = deck_order[x]
        card_name = heka_deck_order[card_order_number]
        ma = heka_deck_values[card_order_number][0]
        #fetu = heka_fetu_values[card_order_number]
        card = Card()
        card.order = card_order_number
        #card.fetu = fetu
        #card.nhk = nhk
        card.ma = ma
        card.name = card_name
        deck.append(card)
    return deck

def generate_random_deck_order():
    deck_order = list(range(52))
    for x in range(52):
        r = (ord(os.urandom(1)) % 52)
        deck_order[x], deck_order[r] = deck_order[r], deck_order[x]
    return deck_order

def wiqa_keysetup(deck):
    k = [0] * 26
    j = 0
    c = 0
    for card in deck:
        k[c] = (k[c] + card.ma) % 26
        j = (j + card.ma) % 26
        c = (c + 1) % 26
    return k, j

def wiqa_sequence_forward(deck, i=26):
    j = 0
    ctxt = []
    c = 0
    k, j = wiqa_keysetup(deck)
    output = []
    for x in range(i):
        j = k[j]
        k[j] = (k[j] - k[c]) % 26
        o = (k[j] + k[k[j]]) % 26
        output.append(o)

    for o in output:
        sub = (o + k[c]) % 26
        ctxt.append(chr(sub + 65))
        c = (c + 1) % 26
    return "".join(ctxt)

def wiqa_sequence_backA(deck, i=26):
    j = 0
    ctxt = []
    c = 0
    k, j = wiqa_keysetup(deck)
    output = []
    for x in range(i):
        j = k[j]
        k[j] = (k[j] - k[c]) % 26
        o = (k[j] + k[k[j]]) % 26
        output.append(o)

    for o in output:
        sub = (o - k[c]) % 26
        ctxt.append(chr(sub + 65))
        c = (c + 1) % 26
    return "".join(ctxt)

def wiqa_sequence_backB(deck, i=26):
    j = 0
    ctxt = []
    c = 0
    k, j = wiqa_keysetup(deck)
    output = []
    for x in range(i):
        j = k[j]
        k[j] = (k[j] - k[c]) % 26
        o = (k[j] + k[k[j]]) % 26
        output.append(o)

    for o in output:
        sub = (k[c] - o) % 26
        ctxt.append(chr(sub + 65))
        c = (c + 1) % 26
    return "".join(ctxt)

def print_card(card):
    print(card.name, card.order, card.fetu, card.ma)

def print_deck(deck):
    for card in deck:
        print_card(card)

def convert_deck_to_msg(deck):
    msg = []
    for card in deck:
        msg.append(chr(card.ma + 65))
    return "".join(msg)

def convert_to_msg(seq):
    msg = []
    for num in seq:
        msg.append(chr(num + 65))
    return "".join(msg)

def get_deck_signature(deck):
    signature = 0
    for card in deck:
        msg.append(chr(card.ma + 65))

def add_decks(decks):
    tmp = list(range(52))
    text = []
    for d in range(len(decks)- 1):
        for x in range(52):
            tmp[x] = (decks[d][x].ma + decks[d+1][x].ma) % 26
            letter = chr(tmp[x] + 65)
            text.append(letter)
    return tmp, "".join(text)

def subtract_decks(decks):
    tmp = list(range(52))
    text = []
    for d in range(len(decks)- 1):
        for x in range(52):
            tmp[x] = (decks[d][x].ma - decks[d+1][x].ma) % 26
            letter = chr(tmp[x] + 65)
            text.append(letter)
    return tmp, "".join(text)

def get_deck_values(deck):
    total = 0
    values = []
    c = 0
    for card in deck:
        v = (card.ma + card.ma + (c*10) + 1) % 26
        values.append(v)
        total += v
        c = (c + 1) % 26
    ma_total = total % 26
    return values, total, ma_total

def binary_sum4bit(h):
    v = 0
    if h[0] == 1:
        v += 8
    if h[1] == 1:
        v += 4
    if h[2] == 1:
        v += 2
    if h[3] == 1:
        v += 1
    return v

def binary_sum8bit(h):
    v = 0
    if h[0] == 1:
        v += 128
    if h[1] == 1:
        v += 64
    if h[2] == 1:
        v += 32
    if h[3] == 1:
        v += 16
    if h[4] == 1:
        v += 8
    if h[5] == 1:
        v += 4
    if h[6] == 1:
        v += 2
    if h[7] == 1:
        v += 1
    return v

def get_fetu_glyphs(deck):
    glyphs = []
    glyphs8 = []
    bin_sums4 = []
    bin_sums8 = []
    bin_sum_total4 = 0
    bin_sum_total8 = 0
    c = 0
    j = 0
    for x in range(int(52 / 4)):
        symbol = []
        for i in range(4):
            g = deck[c].ma % 2
            symbol.append(g)
            c += 1
        v = binary_sum4bit(symbol)
        bin_sums4.append(v)
        bin_sum_total4 += v
        glyphs.append(symbol)

    for x in range(int(52 / 8)):
        symbol8 = []
        for i in range(8):
            g = deck[j].ma % 2
            symbol8.append(g)
            j += 1
        v8 = binary_sum4bit(symbol8)
        bin_sums8.append(v8)
        bin_sum_total8 += v8
        glyphs8.append(symbol8)
    return glyphs, glyphs8, bin_sums4, bin_sum_total4, bin_sums8, bin_sum_total8

def get_fetu_binary_string(glyphs8):
    return bin_string, bin_seq

def load_deck(deck_obj_string):
    deck_obj = deck_obj_string.split()
    deck_order = []
    for x in range(52):
        o = heka_deck_order_rev[deck_obj[x]]
        deck_order.append(o)
    return deck_order

def export_deck(deck):
    names = []
    for card in deck:
        names.append(card.name)
    for name in names:
        sys.stdout.write(name+" ")
    sys.stdout.write("\n")
