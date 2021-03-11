import os
from fetu_cards import *

''' KrypoMagick N Heka Fetu Cards version 'AAB' '''


def main():
    deck_obj_string = input("Enter deck object string: ")
    deck_order = load_deck(deck_obj_string)
    hka_deck = generate_deck(deck_order)
    deck_msg = convert_deck_to_msg(hka_deck)
    ma_values, total, ma_total = get_deck_values(hka_deck)
    glyphsA, glyphs8A, glyph_sums4A, glyph_total4A, glyph_sums8A, glyph_total8A = get_fetu_glyphs(hka_deck)
    wiqa_seqFA = wiqa_sequence_forward(hka_deck)
    wiqa_seqBA = wiqa_sequence_backA(hka_deck)
    wiqa_seqBAB = wiqa_sequence_backB(hka_deck)
    print_deck(hka_deck)
    print(deck_msg)
    print(ma_values, total, ma_total)
    print(wiqa_seqFA, wiqa_seqBA, wiqa_seqBAB)
    print(glyphsA, glyphs8A, glyph_sums4A, glyph_total4A, glyph_sums8A, glyph_total8A)

main()
