from fetu_cards import *
import binascii

itera = 100000
f = open("entropy_pool", "wb")
for x in range(itera):
    tmp_order = generate_random_deck_order()
    tmp_deck = generate_deck(tmp_order)
    bin_sum, bin_sum_hex, bin_msg = get_fetu_binary_message(tmp_deck)
    binary_values, binary_total, max_hex, max_dec, fetu_total, fetu_totals, ovr_dec, ovr_dec_dbl, ovr_dec_dbl_hex, max_squeeze_dec, max_squeeze_hex = fetu_max_entropy(tmp_deck)
    #bin_blob = b''
    #for bbyte in binary_values:
    #    bin_blob += bytes(str(bbyte), "ascii")
    #h = bin_sum_hex[0:len(bin_sum_hex)-1]
    #print(bin_sum_hex)
    #print(len(h), len(max_hex))
    #bin_blob = binascii.unhexlify(h)
    #bin_blob = binascii.unhexlify(bin_sum_hex)
    #print(max_squeeze_hex)
    #msx = max_squeeze_hex
    msx_bite = ovr_dec_dbl_hex[0:len(ovr_dec_dbl_hex) - 1]
    #msx_bite = max_squeeze_hex[0:len(max_squeeze_hex) - 1]
    try:
        bin_blob = binascii.unhexlify(msx_bite)
    except binascii.Error as berr:
        msx_bite += "1"
        bin_blob = binascii.unhexlify(msx_bite)
    f.write(bin_blob)
f.close()
