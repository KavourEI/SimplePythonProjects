from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website_info = website_entry.get()
    useremail_info = email_entry.get()
    pass_info = pass_entry.get()

    if len(website_info) == 0 or len(pass_info) == 0 or len(pass_info) == 0:
        messagebox.showinfo(title="Warning", message="Please fill all the information!")
    else:
         is_ok = messagebox.askokcancel(title=website_info, message=f"Are you sure you want to save: \nEmail :{useremail_info} \nPassword :{pass_info} \n")
         if is_ok:
             with open("data.txt", "a") as f:
                 f.write(f"{website_info} | {useremail_info} | {pass_info} \n")
                 website_entry.delete(0, END)
                 pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels

website = Label(text='Website:')
website.grid(column=0, row=1)

email = Label(text='Email/Username:')
email.grid(column=0, row=2)

password = Label(text='Password:')
password.grid(column=0, row=3)

# Entries

website_entry = Entry(width=37)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=37)
email_entry.insert(END, "themis.kavour@icloud.com")
email_entry.grid(column=1, row=2, columnspan=2)

pass_entry = Entry(width=20)
pass_entry.grid(column=1, row=3)
pass_entry.config()

# Buttons

pass_gen_button = Button(text="Generate Password", command=generate_password)
pass_gen_button.grid(column=2, row=3)

add_button = Button(text='Add', width=37, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()