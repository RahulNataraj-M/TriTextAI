from googletrans import Translator
translator=Translator() #translator is an obj for the class Translator
while(1):
    print("*********************")
    destination=input("Enter the conversion language:")
    inp=input("Enter the input Sentence: ")
    out=translator.translate(inp,dest=destination)
    print(out.text)
    print(out.pronunciation)
    
