import os
import sys
from fetu_cards import *

''' KrypoMagick N Heka Fetu Cards version 'AAH' '''


def main():
    deck_obj_string_file = sys.argv[1]
    f = open(deck_obj_string_file, "r")
    deck_obj_string = f.read()
    f.close()
    deck_order = load_deck(deck_obj_string)
    hka_deck = generate_deck(deck_order)
    deck_msg = convert_deck_to_msg(hka_deck)
    ma_values, total, ma_total = get_deck_values(hka_deck)
    glyphsA, glyph_sums4A, glyph_total4A = get_fetu_glyphs(hka_deck)
    wiqa_seqFA = wiqa_sequence_forward(hka_deck)
    wiqa_seqBA = wiqa_sequence_backA(hka_deck)
    wiqa_seqBAB = wiqa_sequence_backB(hka_deck)
    print("KrypoMagick Fetu Deck Report")
    print("Fetu Deck:")
    print_deck(hka_deck)
    print("Fetu Deck Phrase:", deck_msg)
    print("Fetu Moon Arithmetic (Values, Total MA Total): ")
    print(ma_values, total, ma_total)
    print("Fetu Wiqa Sequences: ")
    print(wiqa_seqFA, wiqa_seqBA, wiqa_seqBAB)
    print("Fetu Binary Sequences: ")
    print(glyphsA, glyph_sums4A, glyph_total4A)

    hexsigintA, hexsig_hexA, bin_msg = get_fetu_binary_message(hka_deck)
    print("Fetu Hex/Binary Signatures: ")
    print(hexsig_hexA, hexsigintA, bin_msg)
    print("\n")

    signatureA, signatureB = get_deck_signature(glyph_total4A, hexsigintA)
    print("Fetu Signatures (A/B): ")
    print(signatureA, signatureB)

    p = nearest_prime(signatureB)
    print("Nearest prime to Signature B: ")
    print(p)

    max_bin, bin_total, max_hex, max_dec, fetu_total, fetu_totals, ovr_dec, ovr_dec_dbl, ovr_dec_dbl_hex, max_squeeze_dec, max_squeeze_hex = fetu_max_entropy(hka_deck)
    print("Max Entropy Function Report --- ")
    print("--- 416 bit entropy extraction --- ")
    print("Hex String: ", max_hex)
    print("Decimal String: ", str(max_dec))
    print("Max Entropy Binary Values: "+str(max_bin))
    print("Max Entropy Binary Total: "+str(bin_total))
    print("Fetu Total: ", str(fetu_total))
    print("Fetu Totals: ", str(fetu_totals))
    print("Overdrive Decimal: ", str(ovr_dec))
    print("Overdrive Decimal Double: ", str(ovr_dec_dbl))
    print("Overdrive Double Hex String: ", str(ovr_dec_dbl_hex))
    print("Max Squeeze Decimal: ", str(max_squeeze_dec))
    print("Max Squeeze Hex String: ", str(max_squeeze_hex))
main()
