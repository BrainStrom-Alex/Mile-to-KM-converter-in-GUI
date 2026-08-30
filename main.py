from tkinter import *

window = Tk()
window.title("Mile to KM Convertor")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)


def converter():
    value = entry.get()
    if value:
        mile = int(value)
        km = mile*1.60
        round_km = round(km, 2)
        label3.config(text=f"{round_km}")

entry = Entry(width=10)
entry.grid(row=0, column=1)

label1 = Label(text="MILE")
label1.grid(row=0, column=2)

label2 = Label(text="is equal to")
label2.grid(row=1, column=0)

label3 = Label()
label3.grid(row=1, column=1)

label4 = Label(text="KM")
label4.grid(row=1, column=2)

button = Button(text="CONVERT", command=converter)
button.grid(row=2, column=1)



window.mainloop()