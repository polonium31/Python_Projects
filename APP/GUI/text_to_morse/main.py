import tkinter as tk


def clearAll():
    input1_data.delete(1.0, tk.END)
    input2_data.delete(1.0, tk.END)


def convert():
    message = input1_data.get("1.0", "end")[:-1]
    result = translate(message)
    input2_data.delete(1.0, tk.END)
    input2_data.insert('end -1 chars', result)


def translate(message):
    encrypt = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
               'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
               'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
               '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-',
               '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '/', '!': '-.-.--',
               '@': '.--.-.', '&': '.-...'}

    decrypt = {v: k for k, v in encrypt.items()}
    if len([i for i in message if i != '-' and i != '.' and i != ' ' and i != '/']) != 0:
        return ' '.join(encrypt[i] for i in message.upper())
    else:
        return ''.join(decrypt[i] for i in message.split())


screen = tk.Tk()
screen.title("TEXT<->MORSE converter")
screen.minsize(width=650, height=650)
screen.config(padx=20, pady=20, bg='#E5DDC8')

# create a global variables
variable1 = tk.StringVar(screen)
variable2 = tk.StringVar(screen)

# initialise the variables
variable1.set("Choose-lang-code")
variable2.set("Choose-lang-code")

# input1 label
input1_label = tk.Label(screen, text="Text input", font=("Montserrat", 22), bg="#E5DDC8")
input1_label.grid(row=0, column=0, padx=10)

# input1
input1_data = tk.Text(screen, width=50, height=10, font=("Courier New", 18))
input1_data.grid(row=0, column=1, pady=10)

# convert Button
convert = tk.Button(screen, text="Convert", command=convert, font=("Montserrat", 18), highlightbackground="#004369",
                    width=10)
convert.grid(row=1, column=1, pady=20)

# input2 label
input2_label = tk.Label(screen, text="Output", font=("Montserrat", 22), bg="#E5DDC8")
input2_label.grid(row=2, column=0, padx=10)
# Morse
input2_data = tk.Text(screen, width=50, height=10, font=("Courier New", 18))
input2_data.grid(row=2, column=1, pady=10)

# clear Button
clear = tk.Button(screen, text="Clear", command=clearAll, font=("Montserrat", 18), highlightbackground="#DB1F48",
                  width=10)
clear.grid(row=3, column=1, pady=10)

screen.mainloop()
