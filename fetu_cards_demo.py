import os
from fetu_cards import *

''' KrypoMagick N Heka Fetu Cards version 'AAG' '''


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

signatureAA, signatureAB = get_deck_signature(glyph_total4A, glyph_total8A)
signatureBA, signatureBB = get_deck_signature(glyph_total4B, glyph_total8B)
print(signatureAA, signatureAB)
print(signatureBA, signatureBB)

p = nearest_prime(signatureAB)
q = nearest_prime(signatureBB)
print(p, q)

''' Modulus Deck '''

hka_orderM = generate_random_deck_order()
hka_deckM = generate_deck(hka_orderM)

ma_valuesM, totalM, ma_totalM = get_deck_values(hka_deckM)
glyphsM, glyphs8M, glyph_sums4M, glyph_total4M, glyph_sums8M, glyph_total8M = get_fetu_glyphs(hka_deckM)

signatureMA, signatureMB = get_deck_signature(glyph_total4M, glyph_total8M)

s = nearest_prime(signatureBB)
print(signatureMB, s)

sigSA = signatureMA % 26
sigSB = signatureMB % 26
print(sigSA, sigSB)

hexsigA, hexsigintA = deck_to_hexstring(hka_deckA)
hexsigB, hexsigintB = deck_to_hexstring(hka_deckB)
print(hexsigA, hexsigintA)
print(hexsigB, hexsigintB)

p1A = pow(totalA, p, hexsigintA)
p1B = pow(totalA, q, hexsigintA)

print(p1A, p1B)

p2A = pow(p1B, p, hexsigintA)
p2B = pow(p1A, q, hexsigintA)
print(p2A, p2B)

p3A = pow(totalB, p, p2A)
p3B = pow(totalB, q, p2B)
print(p3A, p3B)

p4A = pow(p3B, p, p2A)
p4B = pow(p3A, q, p2B)
print(p4A, p4B)
print(totalA, totalB)

print(hexsigA, hexsigintA)
print(hexsigB, hexsigintB)

max_binA, bin_totalA, max_hexA, max_decA, fetu_totalA, fetu_totalsA, ovr_decA, ovr_dec_dblA, ovr_dec_dbl_hexA, max_squeeze_decA, max_squeeze_hexA = fetu_max_entropy(hka_deckA)
max_binB, bin_totalB, max_hexB, max_decB, fetu_totalB, fetu_totalsB, ovr_decB, ovr_dec_dblB, ovr_dec_dbl_hexB, max_squeeze_decB, max_squeeze_hexB = fetu_max_entropy(hka_deckB)
print("Max Entropy Function Report --- ")
print("--- 416 bit entropy extraction --- ")
print("Hex String: ", max_hexA)
print("Decimal String: ", str(max_decA))
print("Max Entropy Binary Values: "+str(max_binA))
print("Max Entropy Binary Total: "+str(bin_totalA))
print("Fetu Total: ", str(fetu_totalA))
print("Fetu Totals: ", str(fetu_totalsA))
print("Overdrive Decimal: ", str(ovr_decA))
print("Overdrive Decimal Double: ", str(ovr_dec_dblA))
print("Overdrive Double Hex String: ", str(ovr_dec_dbl_hexA))
print("Max Squeeze Decimal: ", str(max_squeeze_decB))
print("Max Squeeze Hex String: ", str(max_squeeze_hexB))
print("\n")
print("Hex String: ", max_hexB)
print("Decimal String: ", str(max_decB))
print("Max Entropy Binary Values: "+str(max_binB))
print("Max Entropy Binary Total: "+str(bin_totalB))
print("Fetu Total: ", str(fetu_totalB))
print("Fetu Totals: ", str(fetu_totalsB))
print("Overdrive Decimal: ", str(ovr_decB))
print("Overdrive Decimal Double: ", str(ovr_dec_dblB))
print("Overdrive Double Hex String: ", str(ovr_dec_dbl_hexB))
print("Max Squeeze Decimal: ", str(max_squeeze_decB))
print("Max Squeeze Hex String: ", str(max_squeeze_hexB))
print((((len(max_squeeze_hexB) - 2) / 2) * 8))
