from tkinter import *
from tkinter import messagebox
from pass_gen import PasswordGen
import json
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
pass_class = PasswordGen()


def password():
    entry_pass.delete(0, END)
    curr_pass = pass_class.create_pass()
    entry_pass.insert(0, string=curr_pass)
    pyperclip.copy(curr_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    if len(entry_site.get()) == 0 or len(entry_pass.get()) == 0 or len(entry_email.get()) == 0:
        messagebox.showinfo(title="Empty Entry Bar", message="One of the entry is empty, please fill it.")
    else:
        opt1 = messagebox.askokcancel(title='Save password', message="Do you want to save it or cancel")
        if opt1:
            new_data = {
                entry_site.get(): {
                    "email": entry_email.get(),
                    "password": entry_pass.get(),
                }
            }
            try:
                with open('saved_pass.json', mode='r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('saved_pass.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open('saved_pass.json', mode='w') as file:
                    json.dump(data, file, indent=4)
            finally:
                entry_site.delete(0, END)
                entry_pass.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def search_site():
    try:
        with open('saved_pass.json', mode='r') as file:
            data_dic = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        website = entry_site.get()
        if website in data_dic:
            email = data_dic[website]["email"]
            p_word = data_dic[website]["password"]
            pyperclip.copy(p_word)
            messagebox.showinfo(title="Search Result", message=f"Your email: {email}, \n\nYour password: {p_word}")
        else:
            messagebox.showerror(title="Invalid Search", message="This website don't exist")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

label_site = Label(text='Website:')
label_site.grid(column=0, row=1)

entry_site = Entry(width=34)
entry_site.focus()
entry_site.grid(column=1, row=1)

label_email = Label(text='Email/Username:')
label_email.grid(column=0, row=2)

entry_email = Entry(width=52)
entry_email.insert(index=0, string="gs1306199@gmail.com")
entry_email.grid(column=1, row=2, columnspan=2)

label_pass = Label(text='Password:')
label_pass.grid(column=0, row=3)

entry_pass = Entry(width=34)
entry_pass.grid(column=1, row=3)

btn_pass = Button(text='Generate Password', command=password)
btn_pass.grid(column=2, row=3)

btn_add = Button(text='Add', width=44, command=save_file)
btn_add.grid(row=4, column=1, columnspan=2)

btn_search = Button(text='Search', command=search_site)
btn_search.grid(column=2, row=1)

window.mainloop()
