import tkinter as tk
from tkinter import messagebox


def login():
    username = username_entry.get()
    password = password_entry.get()

    # Примерни потребител и парола
    if username == "admin" and password == "1234":
        messagebox.showinfo("Успех", "Влязохте успешно!")
    else:
        messagebox.showerror("Грешка", "Невалидни данни!")


def toggle_password():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


root = tk.Tk()
root.title("Вход в системата")
root.geometry("400x300")
root.configure(bg="lightgreen")


# Заглавие
title = tk.Label(root, text="Вход", font=("Arial", 20))
title.pack(pady=10)

# Потребителско име
username_label = tk.Label(root, text="Потребителско име:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack(pady=5)

# Парола
password_label = tk.Label(root, text="Парола:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

# Чекбокс за показване на паролата
show_password_var = tk.BooleanVar()
show_password_check = tk.Checkbutton(root, text="Покажи паролата", variable=show_password_var, command=toggle_password)
show_password_check.pack()

# Бутон за вход
login_button = tk.Button(root, text="Вход", command=login, width=15, font=("Arial", 12))
login_button.pack(pady=20)

root.mainloop()
