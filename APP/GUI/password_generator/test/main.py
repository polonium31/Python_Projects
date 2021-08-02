import json
from tkinter import *
from tkinter import messagebox
import pyperclip

# -------------------Random Password-----------------------
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters_list = [random.choice(letters) for _ in range(nr_letters)]
    numbers_list = [random.choice(numbers) for _ in range(nr_numbers)]
    symbols_list = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = letters_list + numbers_list + symbols_list

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)


# -------------------save_entry-----------------------
def add_entry():
    website = entry_website.get()
    email = entry_email_uname.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("util/data.json") as file:
                try:
                    data = json.load(file)
                except json.decoder.JSONDecodeError:
                    data = {}
        except FileNotFoundError:
            with open("util/data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("util/data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


FONT = ("Arial", 20)
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="#f7eab5")

canvas = Canvas(width=280, height=270, bg="#f7eab5", highlightthickness=0)
logo = PhotoImage(file="images/logo.gif")
canvas.create_image(180, 150, image=logo)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:", bg="#f7eab5", font=("Arial",16))
label_website.grid(column=0, row=1)

entry_website = Entry(relief="groove")
entry_website.grid(column=1, row=1, columnspan=1, sticky="EW")
entry_website.focus()


def search_password():
    website = entry_website.get()
    try:
        with open("util/data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="Data not Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="your search details", message=f"email: {email}\npassword: {password}")
        else:
            messagebox.showinfo(title="ERROR", message=f"no details found for this {website}")


search_btn = Button(text="search", width=20, highlightbackground="black", command=search_password,relief="groove")
search_btn.grid(column=2, row=1, columnspan=1, sticky="EW", padx=10, pady=10)

label_email_uname = Label(text="Email/Username:", bg="#f7eab5", font=("Arial",16))
label_email_uname.grid(column=0, row=2)

entry_email_uname = Entry(relief="groove")
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW", padx=2, pady=10)
entry_email_uname.insert(0, "jenu3181@gmail.com")
label_password = Label(text="Password:", font=("Arial",16), bg="#f7eab5")
label_password.grid(column=0, row=3)

entry_password = Entry(relief="groove")
entry_password.grid(column=1, row=3, sticky="EW", padx=1, pady=10)

generate_btn = Button(text="Generate Password", highlightbackground="red", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW", padx=10, pady=10)

add_btn = Button(text="Add", width=35, highlightbackground="black", command=add_entry)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW", padx=2, pady=10)

window.mainloop()
