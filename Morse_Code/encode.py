//This program encrypts a message Using Morse Code

def to_letter_text(text):
   
    code = {
        'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
        'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
        'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
        'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
        '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
        '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
    }
    return ' '.join(code[i] for i in text.lower())
   
text = input("Enter message to encode: ")
print(to_letter_text(text))
