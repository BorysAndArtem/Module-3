import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Привiтання")

def greet():
    label = tk.Label(root, text=f"Добрий день, {entry.get()}")
    label.pack()
btn = tk.Button(root, text="Привiтатись", command=greet)
btn.pack()
entry = tk.Entry(root, width=40)
entry.pack()

root.mainloop()