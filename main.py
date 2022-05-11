import tkinter as tk

window = tk.Tk()
window.title("Hello wold")
window.geometry("500x500")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()
