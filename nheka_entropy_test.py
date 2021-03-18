from fetu_cards import *
import binascii

itera = 100000
f = open("entropy_pool", "wb")
for x in range(itera):
    tmp_order = generate_random_deck_order()
    tmp_deck = generate_deck(tmp_order)
    bin_sum, bin_sum_hex = get_fetu_binary_message(tmp_deck)
    #bin_blob = b''
    #for bbyte in binary_values:
    #    bin_blob += bytes(str(bbyte), "ascii")
    #h = bin_sum_hex[0:len(bin_sum_hex)-1]
    #print(bin_sum_hex)
    #print(len(h), len(max_hex))
    #bin_blob = binascii.unhexlify(h)
    bin_blob = binascii.unhexlify(bin_sum_hex)
    #f.write(bytes("".join(bin_blob)), encoding='ascii')
    f.write(bin_blob)
f.close()
