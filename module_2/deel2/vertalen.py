# def vertaal_word(word):
#     translation_dict = {
#         "Draganthor": "geit",
#         "schubben": "teennagels",
#         "vurige": "waterende",
#         "draak": "geit",
#         "vlammenzee": "golf van water"
#     }
#     return translation_dict.get(word, word)

# def vertaal_sentence(sentence):
#     return " ".join(vertaal_word(word) for word in sentence.split())

# def main():
#     sentence = input("Voer een stukje tekst in: ")
#     vertaalde_sentence = vertaal_sentence(sentence)

#     print("vertaalde tekst:")
#     print(vertaalde_sentence)

# if __name__ == "__main__":
#     main()





















# def vertaal_text(text, translation_dictonary):
#     words = text.split()
#     vertaalde_words = [translation_dictonary.get(word, word) for word in words]
#     return " ".join(vertaalde_words)

vertaal_dictonary = {
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
 
vertaalde_tekst = [vertaal_dictonary.get(woord, woord) for woord in woorden]
#vertaalde_tekst = vertaal_text(originele_tekst, vertaal_dictonary)


 
print("vertaalde tekst:")
print(" ".join(vertaalde_tekst))

