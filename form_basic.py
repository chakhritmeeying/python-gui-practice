import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tkinter Form Practice")
root.geometry("400x300")


def submit_info():
    if not check_show_info.get():
        messagebox.showwarning(
            "Warning", "Please check 'Show Information' to display info.")
        return
    name = name_entry.get()
    age = age_entry.get()
    if not is_valid_input(name, age):
        return
    update_display(name, age)
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


def update_display(name, age):
    selected = radio_var.get()
    if selected == "simple":
        info_text.set(f"Your Information\nName: {name} | Age: {age}")
    else:
        info_text.set(f"Your Information\nName: {name} \n Age: {age}")


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
check_show_info = tk.BooleanVar()
tk.Checkbutton(
    root,
    text="Show Information",
    variable=check_show_info
).pack()

button_frame = tk.Frame(root)
button_frame.pack()

# Radio buttons for display options
radio_var = tk.StringVar(root, "simple")
tk.Radiobutton(
    button_frame,
    text="Simple",
    variable=radio_var,
    value="simple"
).grid(row=0, column=0)
tk.Radiobutton(
    button_frame,
    text="Detail",
    variable=radio_var,
    value="detail"
).grid(row=0, column=1)


# Buttons
tk.Button(
    button_frame,
    text="Submit",
    command=submit_info
).grid(row=1, column=0)
tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields
).grid(row=1, column=1)


# Show info
info_text = tk.StringVar()
tk.Label(
    root,
    textvariable=info_text,
    font=("Arial", 16, "bold")
).pack(pady=10)

root.mainloop()
