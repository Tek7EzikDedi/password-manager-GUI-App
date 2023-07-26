from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except KeyError:
        messagebox.showerror(title="Error", message="No data file found.")
    else:
        if website.get() in data:
            messagebox.showinfo(title=website.get(),message=f"Email: {data[website.get()]['email']} \nPassword: {data[website.get()]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No details for the {website.get()} exists.")





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = [random.choice(letters) for char in range(random.randint(8,10))]
    nr_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    nr_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]

    password_list = nr_letters + nr_symbols + nr_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website.get(): {
            "email": email_username.get(),
            "password": password_entry.get()
        }
    }


    if website.get() == "" or password_entry.get() == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:

                data = json.load(data_file)

                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:

            website.delete(0,END)
            password_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image_lock = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=image_lock)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
website = Entry(width=33)
website.grid(column=1, row=1)
website.focus()

label_email_username = Label(text="Email/Username:")
label_email_username.grid(column=0, row=2)
email_username = Entry(width=52)
email_username.grid(column=1, row=2, columnspan=2)
email_username.insert(0, "fatihhars70@gmail.com")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)



screen.mainloop()