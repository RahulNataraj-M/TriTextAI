from spellchecker import SpellChecker
spell=SpellChecker()  # Create a SpellChecker object to check and correct spelling
while True:
    text=input("Enter the sentence to be corrected: ")
    words=text.split()
    correct_words=[]
    for word in words:
        # If the word is correctly spelled, keep it as is
        if not spell.unknown([word]): 
            correct_words.append(word)
        # If the word is misspelled, append the most likely correction
        else:
            correct_words.append(spell.correction(word))
    correct_text=' '.join(correct_words)
    print(correct_text)
            
