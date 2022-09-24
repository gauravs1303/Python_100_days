from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
fr_word = {}
data = {}

try:
    data_dataframe = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/words_to_learn.csv")
    data = original_data.to_dict(orient='records')
else:
    data = data_dataframe.to_dict(orient='records')


def french_words():
    global flip_timer, fr_word
    window.after_cancel(flip_timer)
    fr_word = random.choice(data)
    canvas.itemconfig(card, image=front_card)
    canvas.itemconfig(label_title, text='French', fill='black')
    canvas.itemconfig(label_word, text=fr_word['French'], fill='black')
    flip_timer = window.after(3000, flip_card, fr_word)


def is_known():
    data.remove(fr_word)
    # Note 1: Index
    pandas.DataFrame(data).to_csv('data/words_to_learn.csv', index=False)
    french_words()


def flip_card(word):
    canvas.itemconfig(card, image=back_card)
    canvas.itemconfig(label_title, text='English', fill='white')
    canvas.itemconfig(label_word, text=word['English'], fill='white')


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, flip_card, fr_word)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file='images/card_front.png')
back_card = PhotoImage(file='images/card_back.png')
card = canvas.create_image(400, 263, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)

label_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, "italic"))
label_word = canvas.create_text(400, 263, text="", font=('Ariel', 60, "bold"))

img_btn_wrong = PhotoImage(file='images/wrong.png')
btn_wrong = Button(image=img_btn_wrong, highlightthickness=0, command=french_words)
btn_wrong.grid(column=0, row=1, pady=50)

img_btn_right = PhotoImage(file='images/right.png')
btn_right = Button(image=img_btn_right, highlightthickness=0, command=is_known)
btn_right.grid(column=1, row=1, pady=50)

# Function to start
french_words()

window.mainloop()
