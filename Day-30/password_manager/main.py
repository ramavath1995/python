import random
from tkinter import *
from tkinter import messagebox
import json


################ Generate Password ######################
def generate_pass():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+']

    password = ""

    a = [random.choice(alphabets) for _ in range(random.randint(6, 8))]
    n = [random.choice(numbers) for _ in range(random.randint(4, 6))]
    s = [random.choice(symbols) for _ in range(random.randint(3, 6))]

    pas = a + n + s
    random.shuffle(pas)
    for i in pas:
        password += i
    password_entry.delete(0, END)
    password_entry.insert(0, string=password)
    password_entry.get()


def save_details():
    website = website_entry.get().title()
    user = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": user,
            "password": password
        }
    }
    if len(password) < 6 or len(user) < 5:
        messagebox.showwarning(title="Oops", message="User name or password should be more than 5 and 6 characters")
    else:
        a = messagebox.askyesno(title="Verification", message="Are you sure want to save details? ")
        if a:
            try:
                with open("password_details.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("password_details.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                # updating data
                data.update(new_data)
                # saving data
                with open("password_details.json", "w") as file:
                    json.dump(data, file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)


def search_password():
    site = website_entry.get().title()
    try:
        with open("password_details.json", "r") as file:
            data = json.load(file)
            if site in data:
                password = data[site]["password"]
                mail = data[site]["email"]
                messagebox.showinfo(title=site, message=f"Email: {mail}\nPassword: {password}")
            else:
                messagebox.showerror(title="Oops", message=f"Site {site} not available in the file")
    except FileNotFoundError:
        messagebox.showerror(title="Oops", message=f"File not found")


############################ Screen setup ####################

bg = "#F7EFE5"
s_blue = "#5B99C2"
purple = "#7C00FE"
green = "#06D001"
pink = "#FF76CE"
maroon = "#F5004F"
black = "#021526"
yellow = "#F9E400"
y = "#FFD35A"
brown = "#820300"

w = Tk()
w.title("Password Manager")
w.config(background=s_blue, pady=50, padx=50)

canvas = Canvas(width=200, height=190, background=s_blue, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 90, image=image)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:", background=y)
website_label.grid(row=1, column=0)
email_label = Label(text="User name/Email:", background=y)
email_label.grid(row=2, column=0)
password_label = Label(text="Password:", background=y)
password_label.grid(row=3, column=0)

website_entry = Entry(width=34)
website_entry.focus_set()
website_entry.grid(row=1, column=1)
email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)
gen_pass_button = Button(text="Generate Password", background=pink, command=generate_pass)
gen_pass_button.grid(row=3, column=2)
search_button = Button(text="Search", width=14, background=green, command=search_password)
search_button.grid(row=1, column=2)

add_button = Button(text="ADD", width=44, background=maroon, command=save_details)
add_button.grid(row=4, column=1, columnspan=2)


w.mainloop()
