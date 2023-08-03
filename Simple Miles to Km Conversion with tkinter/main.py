import tkinter


def button_clicked():
    x = int(dist.get())
    y = x*1.609
    km_value.config(text=y)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20,  pady=20)

# Label
equal_to = tkinter.Label(text="Is equal to", font=('arial', 24))
equal_to.grid(column=0, row=1)

miles = tkinter.Label(text='Miles', font=('arial',24))
miles.grid(column=2, row=0)

km_value = tkinter.Label(text='0', font=('arial', 24))
km_value.grid(column=1, row=1)

km = tkinter.Label(text='Km', font=('arial', 24))
km.grid(column=2, row=1)

# Entry
dist = tkinter.Entry(width=10)
dist.grid(column=1, row=0)

# Button

calc_button = tkinter.Button(text='Calculate', command=button_clicked)
calc_button.grid(column=1, row=2)

window.mainloop()
