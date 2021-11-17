from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    passwrd = "".join(password_list)
    password.insert(0, passwrd)
    pyperclip.copy(passwrd)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():

    website_input = website.get()
    email_input = email.get()
    pass_input = password.get()

    if len(website_input) == 0 or len(pass_input) == 0 or len(email_input) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_input, message=f"These are the details entered: \n "
                                                                    f"Email: {email_input}"
                                                                    f"\nPassword: {pass_input} \nIs it ok to save?")
        if is_ok:
            with open("database.txt", "a") as database:
                database.write(f"{website_input} | {email_input} | {pass_input}\n")
                website.delete(0, END)
                email.delete(0, END)
                password.delete(0, END)
                database.close()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

label_1 = Label(text="Website:")
label_1.grid(column=0, row=1)

website = Entry(width=35)
website.focus()
website.grid(column=1, row=1, columnspan=2)


label_2 = Label(text="Email/Username:")
label_2.grid(column=0, row=2)

email = Entry(width=35)
email.grid(column=1, row=2, columnspan=2)


label_3 = Label(text="Password:")
label_3.grid(column=0, row=3)

password = Entry(width=21)
password.grid(column=1, row=3)


generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(column=2, row=3)

add = Button(text="Add Database", width=36, command=save_data)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()
