import time
import pygame

morse_code = {' ': '_', "'": '.----.', '(': '-.--.-', ')': '-.--.-', ',': '--..--', '-': '-....-', '.': '.-.-.-',
              '/': '-..-.', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
              '6': '-....', '7': '--...','8': '---..', '9': '----.', ':': '---...', ';': '-.-.-.', '?': '..--..',
              'A': '.-', 'B': '-...', 'C': '-.-.','D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
              'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
              'Y': '-.--', 'Z': '--..', '_': '..--.-'}

again=True
time_between=0.5
source="morse_code_audio/"

def con_to_morse(given_text):
    '''Converting function from text to text version of morse code'''
    morse_text=[]
    for symbol in given_text:
        morse_text.append(morse_code[symbol])
    return " ".join(morse_text)

def audio_convert(given_text):
    '''Converting from text given by user to audio version of morse code'''
    pygame.init()
    for symbol in given_text:
        if symbol ==" ":
            print(" " *2, end=" ")
            time.sleep(6*time_between)
        else:
            print(morse_code[symbol.upper()],end=" ")
            pygame.mixer.music.load(source+symbol+'_morse_code.ogg')
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()
            time.sleep(2*time_between)



def play_again():
    global again
    global translate_again
    translate_again = input("Do you want to translate more text? Type Y or N ").lower()
    if translate_again == "y":
        again = True
    elif translate_again == "n":
        again = False
    else:
        print("Wrong input.You need to type Y or N...")
        translate_again = input("Do you want to translate more text? Type Y or N ").lower()



while again:
    choice=input("You wan to translate for text or audio? Type text/audio ...").lower()
    if choice=="text":
        given_text = input("Type text you want to translate (use only symbols from latin alphabet):\n").upper()
        morse=con_to_morse(given_text)
        print(morse)
        play_again()
    elif choice=="audio":
        given_text = input("Type text you want to translate (use only symbols from latin alphabet):\n").upper()
        morse=audio_convert(given_text)
        play_again()
    else:
        print("You need to type text or audio ...")
        choice = input("You wan to translate for text or audio? Type text/audio ...").lower()
