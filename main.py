from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json

# Generate Password
def generate_password():
    entry_password.delete(0, END)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(16))
    entry_password.insert(0, password)
    pyperclip.copy(password)


# Save Password
def save():
    website = entry_website.get()
    email = entry_email_uname.get()
    password = entry_password.get()

    if email == "" or website == "" or password == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail: "
                                                  f"{email} \nPassword: {password} \n\nIs it okay to save?")

        if is_ok:
            new_data = {
                website: {
                    "email": email,
                    "password": password

                }
            }
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)

            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                entry_password.delete(0, END)
                entry_email_uname.delete(0, END)
                entry_website.delete(0, END)



# UI Setup
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50, background="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:", bg="white",)
label_website.grid(column=0, row=1)

entry_website = Entry()
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()

label_email_uname = Label(text="Email/Username:", bg="white")
label_email_uname.grid(column=0, row=2)

entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")

label_password = Label(text="Password:", bg="white")
label_password.grid(column=0, row=3)

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

generate_btn = Button(text="Generate Password", bg="white", command=generate_password, highlightthickness=0)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, bg="white", command=save, highlightthickness=0)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

mainloop()