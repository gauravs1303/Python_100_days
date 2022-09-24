from tkinter import *

window = Tk()
window.minsize(height=130, width=300)
window.title(string='Mile to Km Converter')
window.config(padx=50, pady=20)

convert = Label(text=0)
convert.grid(column=1, row=1)


def mitokm():
    convert.config(text=f'{int(inp.get()) * 1.6}')


mile_lable = Label(text='Miles')
mile_lable.grid(column=2, row=0)

km_lable = Label(text='Km')
km_lable.grid(column=2, row=1)

text_equal = Label(text='is equal to')
text_equal.grid(column=0, row=1)

btn = Button(text="Calculate", command=mitokm)
btn.grid(row=3, column=1)
btn.config(padx=20, pady=0)

inp = Entry(width=10)
inp.grid(column=1, row=0)

window.mainloop()