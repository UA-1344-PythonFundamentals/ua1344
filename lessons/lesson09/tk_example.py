import tkinter as tk

UserList = []
def save():
    name = name_entry.get()
    password = password_entry.get()
    UserList.append({"name": name, "password": password})
    print(UserList)
    update_text()

def update_text():
    text.delete(1.0, tk.END)
    print("Update text")
    for user in UserList:
        print(f"Name: {user['name']}, Password: {user['password']}")
        text.insert(tk.END, f"Name: {user['name']}, Password: {user['password']}\n")

app = tk.Tk()

app.title("My first Tkinter app")
# app.geometry("800x600")
name = tk.Label(app, text="Name")
# name.pack()
name.grid(row=0, column=0)
name_entry = tk.Entry(app)
# name_entry.pack()
name_entry.grid(row=0, column=1)

password = tk.Label(app, text="Password")
# password.pack()
password.grid(row=1, column=0)
password_entry = tk.Entry(app)
# password_entry.pack()
password_entry.grid(row=1, column=1)


button = tk.Button(app, text="Save", command=save)
# button.pack()
button.grid(row=2, column=1)

text = tk.Text(app, height=10, width=30)
# text.pack()   
text.grid(row=3, column=0, columnspan=2)

# update_text()
app.mainloop()


