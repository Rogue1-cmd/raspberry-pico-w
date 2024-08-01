import time
from machine import Pin

led = Pin(15, Pin.OUT)

# timing durations (in seconds)
dot_duration = 0.2  # dot
dash_duration = dot_duration * 3  #dash
intra_character_space = dot_duration  # Space between dots and dashes in the same letter
inter_character_space = dot_duration * 3  # Space between letters
word_space = dot_duration * 7  # Space between words

# Define Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': ' '  # Space character to indicate word space
}

def blink_dot():
    """Function to blink a dot (short blink)."""
    led.value(1) 
    time.sleep(dot_duration)  
    led.value(0)  
    time.sleep(intra_character_space)  # Wait before the next signal

def blink_dash():
    """Function to blink a dash (long blink)."""
    led.value(1)  
    time.sleep(dash_duration)  # Wait for the duration of a dash
    led.value(0)  
    time.sleep(intra_character_space)  # Wait before the next signal

def blink_morse_code(message):
    """Function to blink Morse code for a given message."""
    for char in message.upper():
        if char in morse_code:
            code = morse_code[char]
            for symbol in code:
                if symbol == '.':
                    blink_dot()
                elif symbol == '-':
                    blink_dash()
                elif symbol == ' ':
                    time.sleep(word_space)  # Wait for the duration of a word space
            time.sleep(inter_character_space - intra_character_space)  # Space between characters

message = "Please Help"  
blink_morse_code(message)

