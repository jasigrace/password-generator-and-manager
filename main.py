from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_username_entry.get()
    pwd = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pwd,
        }
    }

    if website == "" or pwd == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as password:
                data = json.load(password)
        except:
            with open("data.json", "w") as password:
                json.dump(new_data, password, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as password:
                json.dump(data, password, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as find:
            data = json.load(find)
    except FileNotFoundError:
        messagebox.showinfo(title=website, message="No Data File Found")
    else:
        if website in data:
            messagebox.showinfo(title=f"{website} Details",
                                message=f"Email: {data[website]['email']}\nPassword: {data[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=70, pady=70)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

# Website Label
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

# Email/Username Label
email_username_label = Label(text="Email/Username: ")
email_username_label.grid(row=2, column=0)

# Password Label
password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)

# Website Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1)
website_entry.focus()

# Search Password Button
search_button = Button(text="Search", command=find_password, width=10)
search_button.grid(row=1, column=2)

# Email/Username Entry
email_username_entry = Entry(width=49)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "jasigraceit9@gmail.com")

# Password Entry
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1)

# Generate Password Button
password_button = Button(text="Generate", command=generate_password, width=10)
password_button.grid(row=3, column=2)

# Add Button
add_button = Button(text="Add", width=42, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
