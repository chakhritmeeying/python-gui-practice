import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter Form Practice")
root.geometry("400x300")


def submit_info():
    name = name_entry.get()
    age = age_entry.get()
    if not is_valid_input(name, age):
        return
    info_text.set(f"Your Information\nName: {name} | Age: {age}")
    clear_confirm = messagebox.askyesno(
        "Confirmation", "Do you want to clear the fields?")
    if clear_confirm:
        reset_form()


def is_valid_input(name, age):
    if not name or not age:
        messagebox.showwarning(
            "Input Error", "Please enter both name and age.")
        return False
    if not age.isdigit():
        messagebox.showwarning(
            "Input Error", "Age must be a number."
        )
        return False
    return True


def clear_fields():
    clear_confirm = messagebox.askyesno(
        "Confirmation", "Do you want to clear the fields?")
    if clear_confirm:
        reset_form()
        info_text.set("")
        messagebox.showinfo("Cleared", "Fields have been cleared.")


def reset_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    name_entry.focus()


tk.Label(
    root,
    text="Enter your information"
).pack()
# Create a frame for information input
information_frame = tk.Frame(root)
information_frame.pack(pady=20)
# Name field
tk.Label(
    information_frame,
    text="Name:"
).grid()
name_entry = tk.Entry(
    information_frame,
    width=20
)
name_entry.grid(row=0, column=1)

# Age field
tk.Label(
    information_frame,
    text="Age:"
).grid(row=1, column=0, pady=10)

age_entry = tk.Entry(
    information_frame,
    width=20
)
age_entry.grid(row=1, column=1)


# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()
tk.Button(
    button_frame,
    text="Submit",
    command=submit_info
).pack(side="left")
tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields
).pack(side="left", padx=10)


# Show info
info_text = tk.StringVar()
tk.Label(
    root,
    textvariable=info_text,
    font=("Arial", 16, "bold")
).pack(pady=10)

root.mainloop()
