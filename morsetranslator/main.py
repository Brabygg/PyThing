import os

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

def main():
    print("The Morse Code Translator")
    print("Developed by Nils K // Brabygg\n")
    while True:
        receive_string()

def receive_string():
    res = input("Input the string you'd like converted to morse code:\n").strip().upper()

    chars = list(res)

    dots = []

    while len(chars) > 0:
        if not chars[0] in char_to_dots:
            input("Your string contains characters that are not present in the international morse code alphabet.\n")
            return
            
        else:
            dots.append(char_to_dots[chars[0]])
    
        chars.pop(0)

    dots = "/".join(dots)
    os.system("cls" if os.name == "nt" else "clear")
    input(dots + "\n")

main()