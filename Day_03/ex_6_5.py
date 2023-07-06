text = "X-DSPAM-Confidence:    0.8475"

placeOfColon = text.find(':')

new_text = text[placeOfColon+1:]

#new_text_nospace = new_text.rstrip()

val = float(new_text)
print(val)