# def translate_word(word):
#     translation_dict = {
#         "Draganthor": "geit",
#         "schubben": "teennagels",
#         "vurige": "waterende",
#         "draak": "geit",
#         "vlammenzee": "golf van water"
#     }
#     return translation_dict.get(word, word)

# def translate_sentence(sentence):
#     return " ".join(translate_word(word) for word in sentence.split())

# def main():
#     sentence = input("Voer een stukje tekst in: ")
#     translated_sentence = translate_sentence(sentence)

#     print("Vertaalde tekst:")
#     print(translated_sentence)

# if __name__ == "__main__":
#     main()





















# def translate_text(text, translation_dict):
#     words = text.split()
#     translated_words = [translation_dict.get(word, word) for word in words]
#     return " ".join(translated_words)

vertaal_dict = {
    'hart': 'ingang',
    'grot': 'grot',
    'zagen': 'zagen',
    'Draganthor': 'Draganthor',
    'glinsterende': 'glinsterende',
    'schubben': 'teennagels',
    'vurige': 'waterende',
    'ogen': 'ogen',
    'draak': 'geit',
    'brulde': 'brulde',
    'spuwde': 'spuwde',
    'vlammenzee': 'golf',
    'hen': 'hen',
    'bedreigde': 'bedreigde',
    'Rurik': 'Rurik',
    'beschermde': 'beschermde',
    'krachtig': 'krachtig',
    'schild': 'zwemvliezen',
    'magie': 'plastic'
}
 
originele_tekst = input("Voer een stukje tekst in: ")
 
woorden = originele_tekst.split()
 
vertaalde_tekst = [vertaal_dict.get(woord, woord) for woord in woorden]
#vertaalde_tekst = translate_text(originele_tekst, vertaal_dict)


 
print("Vertaalde tekst:")
print(" ".join(vertaalde_tekst))