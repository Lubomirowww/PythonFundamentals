import tkinter as tk

def say_hello():
    label.config(text="Обичам те Капи")


root = tk.Tk()
root.title("Пример с tkinter")
root.geometry("1020x800+100+50")

label = tk.Label(root, text="Натисни бутона!",font=("Arial", 18))
label.pack()

button = tk.Button(root, text="Натисни ме", command=say_hello,
                   font=("Arial", 24),
                   width=40, height=10)
button.pack()

root.mainloop()
