import random

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas

current_card = {}
to_learn = {}
try:
    data= pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Hindi", fill="black")
    canvas.itemconfig(card_word, text=current_card["Hindi"], fill="black")
    canvas.itemconfig(old_card, image=card)
    window.after(2500, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(old_card, image=new_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv",index=False)
    next_card()


window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.after(2500, func=flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card = PhotoImage(file="./image/card_front.gif")
new_card = PhotoImage(file="./image/flash_card.gif")
old_card = canvas.create_image(400, 263, image=card)

card_title = canvas.create_text(400, 150, text="Flash Card", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="words",font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
next_card()
wrong_button_image = PhotoImage(file="./image/wrong.gif")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button_image = PhotoImage(file="./image/right.gif")
right_button = Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

window.mainloop()
