import os
from fetu_cards import *

''' KrypoMagick N Heka Fetu Cards version 'AAB' '''


hka_orderA = generate_random_deck_order()
hka_orderB = generate_random_deck_order()
hka_deckA = generate_deck(hka_orderA)
hka_deckB = generate_deck(hka_orderB)
deck_msgA = convert_deck_to_msg(hka_deckA)
deck_msgB = convert_deck_to_msg(hka_deckB)
comb_deck, comb_deck_msg = add_decks([hka_deckA, hka_deckB])
comb_deck_subtracted, comb_deck_msg_s = subtract_decks([hka_deckA, hka_deckB])
ma_valuesA, totalA, ma_totalA = get_deck_values(hka_deckA)
ma_valuesB, totalB, ma_totalB = get_deck_values(hka_deckB)
glyphsA, glyphs8A, glyph_sums4A, glyph_total4A, glyph_sums8A, glyph_total8A = get_fetu_glyphs(hka_deckA)
glyphsB, glyphs8B, glyph_sums4B, glyph_total4B, glyph_sums8B, glyph_total8B = get_fetu_glyphs(hka_deckB)
wiqa_seqFA = wiqa_sequence_forward(hka_deckA)
wiqa_seqBA = wiqa_sequence_backA(hka_deckA)
wiqa_seqBAB = wiqa_sequence_backB(hka_deckA)
print_deck(hka_deckA)
print_deck(hka_deckB)
print(deck_msgA)
print(deck_msgB)
print(comb_deck, comb_deck_msg)
print(comb_deck_subtracted, comb_deck_msg_s)
print(ma_valuesA, totalA, ma_totalA)
print(ma_valuesB, totalB, ma_totalB)
print(wiqa_seqFA, wiqa_seqBA, wiqa_seqBAB)
print(glyphsA, glyphs8A, glyph_sums4A, glyph_total4A, glyph_sums8A, glyph_total8A)
print(glyphsB, glyphs8B, glyph_sums4B, glyph_total4B, glyph_sums8B, glyph_total8B)
export_deck(hka_deckA)
export_deck(hka_deckB)
