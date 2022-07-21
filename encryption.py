
# functions

# cipher function

def cipher(text,key):
    cipher_text=''
    for char in text:
        if char.isalpha():
            char_code=ord(char)+key
            if char.isupper():
                if char_code > 90:
                    char=chr(64+(char_code-90))
                else:
                    char=chr(char_code)
            else:
                if char_code > 122:
                    char=chr(96+(char_code-122))
                else:
                    char=chr(char_code)  
        cipher_text += char
    return cipher_text

 # decipher function
def decipher(text,key):
    plain_text=''
    for char in text:
        if char.isalpha():
            char_code=ord(char)-key
            if char.isupper():
                if char_code < 65:
                    char=chr(91-(65-char_code))
                else:
                    char=chr(char_code)
            else:
                if char_code <97:
                    char=chr(123-(97-char_code))
                else:
                    char=chr(char_code)  
        plain_text += char
    return plain_text   
        
#  getting commad and user input 
user_text = input('Enter our text:..')
try:
    while True:
        user_key=int(input('Enter an integer between 0-25: '))
        if user_key>0 and user_key<=25:
            break
        else:
            print('Please enter collect key \n')
except Exception as e:
    print(e.errno)

while True:
    call_method=input('cipher or decipher ? command: ')
    correct=['cipher','decipher']
    if call_method in correct:
       break
    print('Enter valide method \n')
if call_method == 'cipher':
    print('cipher text is:  ',cipher(user_text,user_key))
else:
     print('original text is:  ',decipher(user_text,user_key))