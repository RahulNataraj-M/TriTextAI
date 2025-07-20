from spellchecker import SpellChecker
spell=SpellChecker()
while True:
    text=input("Enter the sentence to be corrected: ")
    words=text.split()
    correct_words=[]
    for word in words:
        if not spell.unknown([word]):
            correct_words.append(word)
        else:
            correct_words.append(spell.correction(word))
    correct_text=' '.join(correct_words)
    print(correct_text)
            
