from tkinter import *

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

label_email_uname = Label(text="Email/Username:", bg="white")
label_email_uname.grid(column=0, row=2)

entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")

label_password = Label(text="Password:", bg="white")
label_password.grid(column=0, row=3)

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

generate_btn = Button(text="Generate Password", bg="white", highlightthickness=0)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, bg="white", highlightthickness=0)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

mainloop()