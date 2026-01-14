import tkinter as tk

root = tk.Tk()
root.title("Tkinter Form Practice")
root.geometry("400x300")


def show_selected():
    text = f"Your selected option is: {var.get()}"
    label.config(text=text)


var = tk.StringVar(root, "1")


for i in range(1, 5):
    tk.Radiobutton(
        root,
        text=f"Option {i}",
        variable=var,
        value=f"{i}"
    ).pack()

button = tk.Button(
    root,
    text="Show Selected",
    command=show_selected
).pack(pady=20)

label = tk.Label(root)
label.pack()

root.mainloop()
