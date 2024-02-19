#!/usr/bin/env python3

from pythainlp.tokenize import word_tokenize

sentence = "ฉันบอกว่าฉันทำอย่างนั้นไม่ได้"

print(sentence)
print("nmm", word_tokenize(sentence, engine="newmm"))
print("attacut", word_tokenize(sentence, engine="attacut"))
